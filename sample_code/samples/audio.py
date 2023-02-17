'''
Author: Frank Chu
Date: 2023-02-13 18:15:29
LastEditors: Frank Chu
LastEditTime: 2023-02-13 20:08:15
FilePath: /SmartSpeaker/code/audio.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import wave
import sys

import pyaudio

# 每个缓冲区的帧数
# "CHUNK" is the (arbitrarily chosen) number of frames
# the (potentially very long) signals are split into in this example
CHUNK = 1024 

# 采样位数
# 指定了采集音频的数据格式，例如pyaudio.paInt16表示采集16位的整数型音频数据。
FORMAT = pyaudio.paInt16

# 声道：1，单声道；2，双声道 
CHANNELS = 1 if sys.platform == 'darwin' else 2

# 采样频率 frame / seconds Hz // frame * seconds
# 音频文件在计算机中是怎么存储的？逻辑结构是怎么样的？ - Coldwings的回答 - 知乎
# https://www.zhihu.com/question/29261034/answer/78707918
# 先是最简单的PCM/WAV为例，首先它是若干个chunk组成的，
# 这个chunk是什么…你可以姑且认为它是个数据包或者说数据片段。
# chunk 有个 chunk 头，包含一些诸如 chunk 字节数、声道、采样率、位深等信息。
RATE = 44100
RECORD_SECONDS = 5

with wave.open('output.wav', 'wb') as wf:
    
    # 实例化PyAudio 
    p = pyaudio.PyAudio()
    
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, 
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True
                    )

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    stream.close()
    p.terminate()
