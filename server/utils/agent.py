'''
Author: Frank Chu
Date: 2023-02-13 21:35:14
LastEditors: Frank Chu
LastEditTime: 2023-02-25 10:55:49
FilePath: /SmartSpeaker/server/utils/agent.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import os
import openai
import dotenv
import utils.config as config
import utils.recognition_asr as rasp_asr
from utils.edge_tts import tts as rasp_tts
import pygame

dotenv.load_dotenv()

if not config.IS_RASPBERRYPI: import azure.cognitiveservices.speech as speechsdk

openai.api_key = os.getenv("OPENAI_API_KEY")
# import pvcobra
# import dotenv
# from main import recording
# dotenv.load_dotenv()

# speech_end_point = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

class speechAgent:
    # Automatic Speech Recognition https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=macos%2Cterminal&pivots=programming-language-python
    # recognize_from_microphone()，利用微软 Azure 语音转文本 API 将音频实时转换成文本，如果没有声音了，返回文本
    def recognize_from_microphone():
        # print("Meijia is listening...")
        
        # return "this is asr \r\nresult"
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        
        # language configuration
        speech_config.speech_recognition_language= "en-US" if config.LANGUAGE == 'en-US' else "zh-CN"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        
        # To recognize speech from an audio file, use filename instead of use_default_microphone:
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Start recognition
        print("Speak into your microphone.")
        
        # This example uses the recognize_once_async operation to transcribe utterances of up to 30 seconds, or until silence is detected. 
        # For information about continuous recognition for longer audio, including multi-lingual conversations, see How to recognize speech. https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/how-to-recognize-speech?pivots=programming-language-python
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            return ""
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
                return ""
            return ""
        
    def play_file(fileName='hi.mp3', volume = 1):
        pygame.mixer.init()
        
        #loading
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(start=0.0)
        
        while pygame.mixer.music.get_busy():
            pass
        
        pygame.mixer.quit()
        
    # Text-To-Speech
    def tts(res):
        if config.IS_RASPBERRYPI:
            rasp_tts(res)
        else:
            # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
            speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
            audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

            # The language of the voice that speaks.
            # https://speech.microsoft.com/portal/voicegallery
            # speech_config.speech_synthesis_voice_name='zh-CN-YunxiNeural'
            speech_config.speech_synthesis_voice_name='en-US-JennyNeural' if config.LANGUAGE == 'en-US' else 'zh-CN-YunxiNeural'
            

            speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

            # Get text from the console and synthesize to the default speaker.
            text = res

            speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
            
            if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                # print("Speech synthesized for text [{}]".format(text))
                print("Speech synthesized finished")
                return
            elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_synthesis_result.cancellation_details
                print("Speech synthesis canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    if cancellation_details.error_details:
                        print("Error details: {}".format(cancellation_details.error_details))
                        print("Did you set the speech resource key and region values?")

        # print(f"Meijia is saying: {res}")
        os.system(f'espeak-ng -v "yue" "{res}"') if config.IS_RASPBERRYPI else os.system(f'say -v "Mei-Jia" "{res}"')
        
    
class chatGPTAgent:
    # ask chat gpt

    def chatGPT(text):
        def ask(question):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{question}",
                temperature=0.6,
                max_tokens=2048,
            )
            return f"{response.choices[0].text.strip()}"
        
        if text is None or text == '':
            print("error => ars speech to text failure.")
            return '没有听清楚，再说一遍吧。'
        text = text.replace('\n', '').replace('\r', '').strip()
        res = ask(text)
        return res