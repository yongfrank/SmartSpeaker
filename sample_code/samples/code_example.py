'''
Author: Frank Chu
Date: 2023-02-13 19:58:45
LastEditors: Frank Chu
LastEditTime: 2023-02-16 19:31:16
FilePath: /SmartSpeaker/code/samples/code_example.py
Description: 
https://mp.weixin.qq.com/s/ozGhxHxUhY_fYKgv2fhNUg


Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import pvporcupine
import struct
import pyaudio
import pvcobra
import time
import os
import speech_recognition as sr
from agent import chatGPTAgent as gpt
from agent import speechAgent as speech
from utils.logger import logger


porcupine = None
pa = None
audio_stream = None
r = sr.Recognizer()


def picovoice():
    access_key = 'your key'
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['your path']
    )
    pa = pyaudio.PyAudio()
    cobra = pvcobra.create(access_key)
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        #
        _pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(_pcm)
        if keyword_index >= 0:
            run()


def chatGPT(text):
    if len(text) == 0:
        return
    text = text.replace('\n', ' ').replace('\r', '').strip()
    logger.info(f'chatGPT Q: {text}')
    res = gpt.ask(text)
    logger.info(f'chatGPT A: {res}')
    return res


def run():
    logger.info('start recognize_from_microphone')
    q = speech.recognize_from_microphone()
    logger.info(f'recognize_from_microphone, text={q}')
    res = chatGPT(q)
    # os.system(f'say -v "Mei-Jia" "{res}"')
    speech.tts(res)


picovoice()