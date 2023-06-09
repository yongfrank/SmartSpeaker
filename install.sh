#!/bin/bash
###
 # @Author: Frank Chu
 # @Date: 2023-02-13 20:13:39
 # @LastEditors: Frank Chu
 # @LastEditTime: 2023-03-03 18:05:52
 # @FilePath: /SmartSpeaker/install.sh
 # @Description: 
 # 
 # Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
### 

# Uncomment to install nvm
# https://github.com/nvm-sh/nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
nvm install 16

cd ./client && npm install
cd ../server && pip install -r requirements.txt
mv .env.example .env

sudo apt-get update

# https://stackoverflow.com/questions/58974116/how-to-install-libasound2-dev-32-bit-without-using-apt-get
sudo apt-get install libportaudio2

# https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
sudo apt-get install espeak-ng

pip install azure-cognitiveservices-speech
pip install pygame
pip install speechrecognition

# sudo apt-get install build-essential libasound2 wget libssl-dev
sudo apt-get install build-essential libasound2 wget 



# #requirements.txt?
# pip3 install pyAudio
# # sudo apt install python3-pyaudio
# pip3 install pvporcupine
# pip3 install python-dotenv
# pip3 install keyboard
# pip3 install pvcobra

# # https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cpypi#platform-requirements
# pip3 install azure-cognitiveservices-speech
# pip3 install openai