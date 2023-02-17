#!/bin/bash
###
 # @Author: Frank Chu
 # @Date: 2023-02-13 20:13:39
 # @LastEditors: Frank Chu
 # @LastEditTime: 2023-02-17 01:21:59
 # @FilePath: /SmartSpeaker/install.sh
 # @Description: 
 # 
 # Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
### 

#requirements.txt?
pip3 install pyAudio
# sudo apt install python3-pyaudio
pip3 install pvporcupine
pip3 install python-dotenv
pip3 install keyboard
pip3 install pvcobra

# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi#platform-requirements
pip3 install azure-cognitiveservices-speech
pip3 install openai