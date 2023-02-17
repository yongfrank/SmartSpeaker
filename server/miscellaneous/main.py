'''
Author: Frank Chu
Date: 2023-02-13 20:08:33
LastEditors: Frank Chu
LastEditTime: 2023-02-17 00:58:11
FilePath: /SmartSpeaker/server/main.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import os
import pvporcupine
import pyaudio
import struct

from utils.agent import speechAgent as speech
from utils.agent import chatGPTAgent as gpt
import utils.config as config
from utils.logger import logger

# .env file https://bornforthis.cn/posts/19.html
from dotenv import load_dotenv
load_dotenv()

# import speech_recognition as sr

# def get_next_audio_frame():
#     pass

# recording = False
# porcupine = None
# pa = None
# audio_stream = None
# r = sr.Recognizer()

def chatGPT(text):
    if len(text) == 0:
        print("error => ars speech to text failure.")
        return
    text = text.replace('\n', '').replace('\r', '').strip()
    print(text)
    res = gpt.ask(text)
    return res

def run():
    question = speech.recognize_from_microphone()
    print(f'recognize_from_microphone, text={question}')
    res = chatGPT(question)
    speech.tts(res)
    # recording = False

def picovoice():
    
    # https://picovoice.ai/docs/quick-start/porcupine-python/
    # ['picovoice', 'Hello-Pie_en_mac_v2_1_0/Hello-Pie_en_mac_v2_1_0.ppn']
    if config.TEST_MODE:
        porcupine = pvporcupine.create(
            access_key=config.PICOVOICE_AI_KEY,
            keywords=['picovoice']
        )
    else:
        porcupine = pvporcupine.create(
            access_key=config.PICOVOICE_AI_KEY,
            keyword_paths=["hellomoss_raspberrypi.ppn"] if config.IS_RASPBERRYPI else ["hellopie_macos.ppn"]
        )
    
    pa = pyaudio.PyAudio()
    
    # 打开一个流，设置流的参数，采样率，帧大小
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    
    while True:
        
        # read from trained model: porcupine
        # audo_strem open from pyaudio
        pcm = audio_stream.read(num_frames=porcupine.frame_length, exception_on_overflow=False)
        
        # unpack from struct 
        # import struct
        audio_fram_pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        
        # if not recording:
        keyword_index = porcupine.process(audio_fram_pcm)
        if keyword_index < 0:
            continue
        elif keyword_index == 0:
            print("detected picovoice") if config.TEST_MODE else print("detected hello pie")
            logger.debug('hi')
            # run()
        elif keyword_index == 1:
            print("# detected `bumblebee`")
        # else:
        #     is_voiced = cobra_handle.process(audio_fram_pcm)
        #     silence_count = 0 if is_voiced > 0.5 else silence_count + 1
        #     if silence_count <= 50:
        #         if silence_count < 10:
        #             buffer.append(pcm)
        #         else:
        #             s = time.time()
        #     else:
        #         recording = False
    
    # porcupine.delete()
    
picovoice()



