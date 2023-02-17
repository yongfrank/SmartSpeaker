'''
Author: Frank Chu
Date: 2023-02-16 19:15:19
LastEditors: Frank Chu
LastEditTime: 2023-02-17 01:00:43
FilePath: /SmartSpeaker/server/utils/app_object.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import utils.config as config
import pvporcupine
import pyaudio

class App_object:
    def porcupine_init():
        if config.TEST_MODE:
            porcupine = pvporcupine.create(
                access_key=config.PICOVOICE_AI_KEY,
                keywords=[config.TEST_TRIGGER_WORD]
            )
        else:
            porcupine = pvporcupine.create(
                access_key=config.PICOVOICE_AI_KEY,
                keyword_paths=[config.RASPBERRYPI_PPN] if config.IS_RASPBERRYPI else [config.MACOS_PPN]
            )
        return porcupine

    def audio_stream_init(porcupine):
        pa = pyaudio.PyAudio()
        
        # 打开一个流，设置流的参数，采样率，帧大小
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        return audio_stream
    porcupine = porcupine_init()
    audio_stream = audio_stream_init(porcupine=porcupine)
    