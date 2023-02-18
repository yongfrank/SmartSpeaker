'''
Author: Frank Chu
Date: 2023-02-16 18:33:54
LastEditors: Frank Chu
LastEditTime: 2023-02-18 19:56:03
FilePath: /SmartSpeaker/server/app.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import struct
import threading

from utils.app_object import App_object
from utils.agent import speechAgent as speech
from utils.agent import chatGPTAgent as gpt

import utils.state_of_system as state
import utils.config as config
from utils.edge_tts import tts as rasp_tts
from utils.recognition_asr import asr as rasp_asr


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def main_speaker_process():
    
    def run():
        question = rasp_asr() if config.IS_RASPBERRYPI else speech.recognize_from_microphone()
        socketio.emit('state', { 'state': state.ASR_END, 'value' : question })
        
        res = gpt.chatGPT(question)
        socketio.emit('state', { 'state': state.GPT_END, 'value': res } )
        
        rasp_tts(res) if config.IS_RASPBERRYPI else speech.tts(res)
        socketio.emit('state', { 'state': state.TTS_END, 'value': ""} )
        # recording = False
    
    # https://picovoice.ai/docs/quick-start/porcupine-python/
    # ['picovoice', 'Hello-Pie_en_mac_v2_1_0/Hello-Pie_en_mac_v2_1_0.ppn']
    app_object = App_object()
    
    while True:
        # read from trained model: porcupine
        # audo_strem open from pyaudio
        pcm = app_object.audio_stream.read(num_frames=app_object.porcupine.frame_length, exception_on_overflow=False)
        
        # unpack from struct 
        # import struct
        audio_fram_pcm = struct.unpack_from("h" * app_object.porcupine.frame_length, pcm)
        
        # if not recording:
        keyword_index = app_object.porcupine.process(audio_fram_pcm)
        if keyword_index < 0:
            continue
        elif keyword_index == 0:
            print("detected picovoice") if config.TEST_MODE else print("detected hello pie")
            socketio.emit('state', { 'state' : state.TRIGGER, 'value' : "" })
            run()
            socketio.emit('state', { 'state' : state.RUNNING, 'value' : "" })
    
def send_time():
    while True:
        time_now = time.strftime('%H:%M:%S')
        # print(time_now)
        socketio.emit('time', { 'time': time_now } )
        socketio.sleep(1)


if __name__ == '__main__':
    socketio.start_background_task(send_time)
    thread = threading.Thread(target=main_speaker_process)
    thread.start()
    socketio.run(app, host='0.0.0.0', port=3001)