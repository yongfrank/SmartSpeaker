'''
Author: Frank Chu
Date: 2023-02-18 18:38:58
LastEditors: Frank Chu
LastEditTime: 2023-02-18 19:48:40
FilePath: /SmartSpeaker/sample_code/voice_helper_with_recog.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import speech_recognition as sr

def asr():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        # https://github.com/Uberi/speech_recognition/issues/481
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source, phrase_time_limit=10)

    # recognize speech using Microsoft Azure Speech
    AZURE_SPEECH_KEY = "9834565be2384ffdbdf75d2ff100425f"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    print("end recording")
    try:
        res = r.recognize_azure(audio, key=AZURE_SPEECH_KEY, language="zh-CN", location="eastasia")
        print(res[0])
        return res[0]
    except sr.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Azure Speech service; {0}".format(e))
        
print(asr())