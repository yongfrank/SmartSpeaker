'''
Author: Frank Chu
Date: 2023-02-16 20:46:01
LastEditors: Frank Chu
LastEditTime: 2023-02-16 20:52:38
FilePath: /SmartSpeaker/sample_code/parallel.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
# Import modules
from flask import Flask, request
from flask_socketio import SocketIO, emit
import time

# Create app and socketio objects
app = Flask(__name__)
socketio = SocketIO(app)

# Define a function to print time every one second and emit it to the client if connected
def print_time1():
    while True:
        time_now = time.strftime('%H:%M:%S')
        print(time_now)
        socketio.emit('time', {'time': time_now})
        socketio.sleep(1)


# Define a function to print IP address every one second and emit it to the client if connected
def print_time2():
    while True:
        time_now = time.strftime('%M:%S')
        print(time_now)
        socketio.emit('time', {'time': time_now})
        socketio.sleep(0.1)

# Define a route for the index page
@app.route('/')
def index():
    return "Hello, world!"

# Define a handler for when a client connects
@socketio.on('connect')
def handle_connect():
    print("Client connected")

# Start two background tasks for printing time and IP address 
socketio.start_background_task(print_time1)
socketio.start_background_task(print_time2)

# Run the app with socketio 
if __name__ == '__main__':
    socketio.run(app)