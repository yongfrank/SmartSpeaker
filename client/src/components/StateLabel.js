/*
 * @Author: Frank Chu
 * @Date: 2023-02-17 13:04:51
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-17 13:36:43
 * @FilePath: /SmartSpeaker/client/src/components/StateLabel.js
 * @Description: https://www.npmjs.com/package/react-ts-typewriter
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */
import TypeWriter from 'react-ts-typewriter'

const StateLabel = ({state, speed = 30}) => {
    
    return (
        <>
            <TypeWriter text={state} cursor='' speed={speed}/>
        </>
    )
}

export default StateLabel