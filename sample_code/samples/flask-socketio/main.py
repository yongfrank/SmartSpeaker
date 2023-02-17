'''
Author: Frank Chu
Date: 2023-02-16 15:43:01
LastEditors: Frank Chu
LastEditTime: 2023-02-16 15:44:20
FilePath: /SmartSpeaker/code/samples/flask-socketio/main.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)

if __name__ == '__main__':
    socketio.run(app)