import React from 'react';
import set_icon from '../Header/img/settingicon.png';
import ballon_icon from '../Header/img/ballonicon.png';
import './Bar.css'
import { Link } from 'react-router-dom';

function Bar(props) {
    return(
        <div className="bar">
            {props.children}
        </div>
    );
}

export default Bar