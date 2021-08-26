import React from 'react';
import './DetailPageRecentInfoListCard.css'


function RecentInfoListCard(props) {
    return(
    <div className="DP_card">
        <div className="DP_divisionBox"></div>
        <div className="DP_info">
            <div className="DP_title">bitcoin 호재 업로드 날짜</div>
            <div className="DP_sub">
                <div className="DP_source">구글뉴스</div>
                <div className="DP_time">
                    <div className="DP_uploadTime">upload.date / 08.24</div>
                    <div className="DP_releaseTime">release.date / 09.17</div>
                </div>
            </div>
        </div>
    </div>
    );
}

export default RecentInfoListCard