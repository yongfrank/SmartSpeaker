'''
Author: Frank Chu
Date: 2023-02-14 13:49:04
LastEditors: Frank Chu
LastEditTime: 2023-02-14 23:26:01
FilePath: /SmartSpeaker/code/samples/myproject/hello.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>hello world!</p>"
    # return __name__
    
@app.route("/<name>")
def hello(name):
    # return f"hello {escape(name)}!"
    return f"hello {escape(name)}"