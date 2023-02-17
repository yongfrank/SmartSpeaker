/*
 * @Author: Frank Chu
 * @Date: 2023-02-16 19:34:04
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-17 17:07:37
 * @FilePath: /SmartSpeaker/client/src/App.js
 * @Description: https://mhnpd.github.io/react-loader-spinner/docs/components/tail-spin React Spinners
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */
import './App.css';
import io from 'socket.io-client';
import { useState, useEffect } from 'react';

import ClockComponent from './components/ClockComponent'
import { Bars, Circles, CirclesWithBar, TailSpin, ThreeDots } from 'react-loader-spinner'
import StateLabel from './components/StateLabel';

const socket = io.connect('http://franks-macbook-pro.local:3001/')
// const stringExample = 'There is a known issue on Windows 11 that might affect some types of Secure Sockets Layer (SSL) and Transport Layer Security (TLS) connections. For more information, see the troubleshooting guide.'
const State = Object.freeze({
  UNKNOWN: { name: 'unknown' },
  RUNNING: { name: 'running' },
  TRIGGER: { name: 'trigger' },
  ASR_END: { name: 'asr_end' }, 
  GPT_END: { name: 'gpt_end' },
  SOUND_END: { name: 'tts_end' }
});

function App() {
  const [appState, setAppState] = useState(State.UNKNOWN.name)
  const [labelValue, setLabelValue] = useState({ 'question': '', 'answer': ''})
  const [time, setTime] = useState('??:??:??');

  useEffect(() => {
    let isRunning = false
    socket.on('time', (data) => {
      setTime(data.time)
      if (!isRunning) { setAppState(State.RUNNING.name); isRunning = true }
    })
    
    socket.on('state', data => {
      if (data.state === State.TRIGGER.name ) { setLabelValue({ 'question': '', 'answer': '' }) }
      // const result = Object.values(State).find(item => item.name === data.state).name || State.UNKNOWN.name
      
      const result = data.state
      const value = data.value
      if ( data.state === State.ASR_END.name ) { setLabelValue({ 'question': value, 'answer': '' }) }
      if ( data.state === State.GPT_END.name ) { setLabelValue(pre => { return {'question': pre.question, 'answer': value } }) }

      setAppState(result)
    })
    socket.on('disconnect', () => {
      setAppState(State.UNKNOWN.name)
      setTime('??:??:??')
      isRunning = false
    })
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <ClockComponent timeIsShowing={time}/>

        <div style={{padding: '1em'}}>
          {/* <SoundWave isShowing={appState === State.RUNNING.name ? true : false} /> */}
          { appState === State.UNKNOWN.name ? <TailSpin /> : false }
          { appState === State.RUNNING.name ? <Circles /> : false }
          { appState === State.TRIGGER.name ? <Bars /> : false }
          { appState === State.ASR_END.name ? <ThreeDots /> : false }
          { appState === State.GPT_END.name ? <CirclesWithBar /> : false }
        </div>

        <div className='Label'>
            { labelValue.question !== '' ? <div className='Question'><StateLabel state={labelValue.question}/></div> : false }
          {/* <div className='Question'>

            <StateLabel state={stringExample}/>
          </div> */}
          
            { labelValue.answer !== '' ? <div className='Answer'><StateLabel state={labelValue.answer} speed={150}/></div> : false }
          {/* <div className='Answer'>
            <StateLabel state={stringExample}/>
          </div> */}
        </div>
        
      </header>
    </div>
  );
}

export default App;
