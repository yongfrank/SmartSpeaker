'''
Author: Frank Chu
Date: 2023-02-18 17:12:38
LastEditors: Frank Chu
LastEditTime: 2023-02-18 17:28:43
FilePath: /SmartSpeaker/sample_code/voice_generator.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import asyncio
import pygame
import edge_tts

def play_local_file(file, volume = 1):
    pygame.mixer.init()
    
    #loading
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(start=0.0)
    
    while pygame.mixer.music.get_busy():
        pass
    
    pygame.mixer.quit()
    
async def _main(TEXT, VOICE, OUTPUT_FILE) -> None:
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
    asyncio.get_event_loop().run_until_complete(_main(TEXT=text, VOICE=VOICE, OUTPUT_FILE=OUTPUT_FILE))
    play_local_file(OUTPUT_FILE)
    
tts("嗨")
