'''
Author: Frank Chu
Date: 2023-02-13 21:35:14
LastEditors: Frank Chu
LastEditTime: 2023-02-17 13:43:43
FilePath: /SmartSpeaker/server/utils/agent.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import os
import azure.cognitiveservices.speech as speechsdk
import openai
import dotenv

dotenv.load_dotenv()

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
        speech_config.speech_recognition_language="zh-CN"

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
        
    
    # Text-To-Speech
    def tts(res):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='zh-CN-YunxiNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Get text from the console and synthesize to the default speaker.
        text = res

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
        
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

        # print(f"Meijia is saying: {res}")
        # os.system(f'say -v "Mei-Jia" "{res}"')
    
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
        
        if len(text) == 0:
            print("error => ars speech to text failure.")
            return
        text = text.replace('\n', '').replace('\r', '').strip()
        res = ask(text)
        return res