/*
 * @Author: Frank Chu
 * @Date: 2023-02-16 23:32:50
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-17 00:18:24
 * @FilePath: /SmartSpeaker/client/src/components/SoundWave.js
 * @Description: https://youtu.be/gnelOzlWn7c Stunning Sound Wave Animation with only CSS3
 * CSS3 - Music Waves Loading Animation | Webkit Coding https://youtu.be/WXjrZ93hNgc
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */
import "./sound.css"

const SoundWave = ({ isShowing }) => {
    if (isShowing === true) {
        return (
            <div className="loader">
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
            </div>
        )
    } else {
        return (
            <div className="emptyclass">
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
                <span className="stroke"></span>
            </div>
        )
    }
}

export default SoundWave