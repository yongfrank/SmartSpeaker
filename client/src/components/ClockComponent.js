/*
 * @Author: Frank Chu
 * @Date: 2023-02-16 22:38:10
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-16 23:12:17
 * @FilePath: /SmartSpeaker/client/src/components/ClockComponent.js
 * @Description: https://youtu.be/RmnUaGOsYdc Build a digital clock with React (Beginner React Project)
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */
import "./clock.css"

const ClockComponent = ({ timeIsShowing }) => {
    return (
        <div className="clock">
            <div className='screen'>
                <h1 className='time'>{timeIsShowing}</h1>
            </div>
        </div>
    )
}

export default ClockComponent