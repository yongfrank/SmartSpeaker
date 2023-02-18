'''
Author: Frank Chu
Date: 2023-02-18 17:29:05
LastEditors: Frank Chu
LastEditTime: 2023-02-18 17:43:50
FilePath: /SmartSpeaker/server/utils/edge_tts.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import asyncio
import pygame
import edge_tts

# 【树莓派-微软TTS-多模型文本转语音】 https://www.bilibili.com/video/BV1T3411n7Uu/?share_source=copy_web&vd_source=bf4952280cde801b178268abc99a7047
def play_local_file(file, volume = 1):
    pygame.mixer.init()
    
    #loading
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(start=0.0)
    
    while pygame.mixer.music.get_busy():
        pass
    
    pygame.mixer.quit()
    
async def getFile(TEXT, VOICE, OUTPUT_FILE) -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                pass
                # print(f"WordBoundary: {chunk}")

def tts(text):
    OUTPUT_FILE = "test.mp3"
    VOICE = "zh-CN-YunxiNeural"
    
    # https://stackoverflow.com/questions/48725890/runtimeerror-there-is-no-current-event-loop-in-thread-thread-1-multithreadi
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    asyncio.get_event_loop().run_until_complete(getFile(TEXT=text, VOICE=VOICE, OUTPUT_FILE=OUTPUT_FILE))
    play_local_file(OUTPUT_FILE)