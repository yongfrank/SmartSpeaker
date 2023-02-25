'''
Author: Frank Chu
Date: 2023-02-18 18:32:04
LastEditors: Frank Chu
LastEditTime: 2023-02-25 10:24:47
FilePath: /SmartSpeaker/server/utils/recognition_asr.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import speech_recognition as sr
import utils.config as config

def asr():
    # obtain audio from the microphone
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        # https://github.com/Uberi/speech_recognition/issues/481
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source, phrase_time_limit=15)

    print("end recording")
    # recognize speech using Microsoft Azure Speech
    AZURE_SPEECH_KEY = config.SPEECH_KEY  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    try:
        res = r.recognize_azure(audio, key=AZURE_SPEECH_KEY, language="zh-CN", location=config.SPEECH_REGION)
        # res = r.recognize_azure(audio, key=AZURE_SPEECH_KEY, language="en-US", location=config.SPEECH_REGION)
        print(res[0])
        return res[0]
    except sr.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Azure Speech service; {0}".format(e))