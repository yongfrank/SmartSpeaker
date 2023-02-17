/*
 * @Author: Frank Chu
 * @Date: 2023-02-14 23:29:45
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-16 18:33:10
 * @FilePath: /SmartSpeaker/code/samples/react-flask-app/src/App.js
 * @Description: https://juejin.cn/post/6976498230485860382 创建 React + Flask 前后端分离项目
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */

import React, { useState } from 'react';
import io from 'socket.io-client';

const socket = io.connect('http://localhost:3001');

function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);

  const sendChat = (e) => {
    e.preventDefault();
    socket.emit('message', message);
    setMessage('');
  };

  socket.on('message', (msg) => {
    setChat([...chat, msg]);
  });

  const [time, setTime] = useState('');
  socket.on('time', (data) => {
    setTime(data.time)
  })

  return (
    <div className="App">
      <h1>React + Flask + Socket.IO Chat</h1>
      <p>{time}</p>
      <form onSubmit={sendChat}>
        <input
          type="text"
          name="chat"
          placeholder="Type a message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
      <div className="chat-box">
        {chat.map((msg, index) => (
          <p key={index}>{msg}</p>
        ))}
      </div>
    </div>
  );
}

export default App;