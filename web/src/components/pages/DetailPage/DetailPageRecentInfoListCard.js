import { Divider } from 'antd';
import React from 'react';
import './DetailPageRecentInfoListCard.css'


function RecentInfoListCard(props) {
    var now = new Date();
    var upload_date = new Date(props.upload_date);
    var diff = Math.abs(now.getTime() - upload_date.getTime());
    var time = Math.ceil(diff/(1000*3600*24));
    if(time<1){
        time = Math.ceil(diff/(1000*60*24)) + '시간 전';
    }
    else{
        time = time + '일 전';
    }
    var release_date = props.release_date.substr(0,10) ;
    if(release_date == ''){
        release_date = '--';
    }
    return(
    <a href={props.link} style={{color:'rgb(0,0,0)' ,textDecoration:'none'}}>
    <div className="DP_card">
        <div className="DP_info">
            <div className="DP_title">{props.title}</div>
            <div className="DP_sub">
                <div className="DP_source">{props.source}</div>
                <div className="DP_time">
                    <div className="DP_uploadTime">{time}</div>
                    <div className="DP_releaseTime">{'release date: ' + release_date}</div>
                </div>
            </div>
        </div>
    </div>
    </a>
    );
}

export default RecentInfoListCard