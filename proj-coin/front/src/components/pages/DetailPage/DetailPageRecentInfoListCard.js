import React from 'react';
import './DetailPageRecentInfoListCard.css'


function RecentInfoListCard(props) {
    return(
    <div className="DP_card">
        <div className="DP_divisionBox"></div>
        <div className="DP_info">
            <div className="DP_title">{props.title}</div>
            <div className="DP_sub">
                <div className="DP_source">{props.source}</div>
                <div className="DP_time">
                    <div className="DP_uploadTime">{props.upload_date}</div>
                    <div className="DP_releaseTime">{props.realease_date}</div>
                </div>
            </div>
        </div>
    </div>
    );
}

export default RecentInfoListCard