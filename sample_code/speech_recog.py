'''
Author: Frank Chu
Date: 2023-02-18 18:25:31
LastEditors: Frank Chu
LastEditTime: 2023-02-18 18:38:48
FilePath: /SmartSpeaker/sample_code/speech_recog.py
Description: https://blog.csdn.net/m0_57307642/article/details/120849915 
SpeechRecogintion 是 Python 的一个语音识别框架，
它可以检测语音中的停顿自动终止录音并保存，比 PyAudio 更人性化，很适合语音助手。

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import speech_recognition as sr   #pyaudio SpeechRecognition模块

def rec(rate=16000):     #从系统麦克风拾取音频数据，采样率为 16000
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")  #这里会打印please say something，提示你说话进行录音
        audio = r.listen(source)   

    with open("recording.wav", "wb") as f:   #把采集到的音频数据以 wav 格式保存在当前目录下的recording.wav 文件
        f.write(audio.get_wav_data())
    return 1
    
rec()  #运行rec函数，录制音频