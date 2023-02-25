'''
Author: Frank Chu
Date: 2023-02-16 18:40:52
LastEditors: Frank Chu
LastEditTime: 2023-02-25 10:53:45
FilePath: /SmartSpeaker/users/yongfrank/developer/smartspeaker/server/utils/config.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import dotenv
import os

dotenv.load_dotenv()

PICOVOICE_AI_KEY = os.getenv('PICOVOICE_AI_KEY')
SPEECH_KEY = os.getenv('SPEECH_KEY')
SPEECH_REGION = os.getenv('SPEECH_REGION')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

TEST_MODE = False
IS_RASPBERRYPI = False
# IS_RASPBERRYPI = True

TEST_TRIGGER_WORD = 'picovoice'
RASPBERRYPI_PPN = 'hellomoss_raspberrypi.ppn'
MACOS_PPN = 'hellopie_macos.ppn'
LANGUAGE = 'en-US'