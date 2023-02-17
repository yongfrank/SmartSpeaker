'''
Author: Frank Chu
Date: 2023-02-14 23:32:33
LastEditors: Frank Chu
LastEditTime: 2023-02-16 18:31:06
FilePath: /SmartSpeaker/code/samples/react-flask-app/api/app.py
Description: 创建 React + Flask 前后端分离项目 https://juejin.cn/post/6976498230485860382

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('message', data, broadcast=True)

def send_time():
    while True:
        time_now = time.strftime('%H:%M:%S')
        print(time_now)
        socketio.emit('time', {'time': time_now})
        socketio.sleep(1)

if __name__ == '__main__':
    socketio.start_background_task(send_time)
    socketio.run(app, port=3001)