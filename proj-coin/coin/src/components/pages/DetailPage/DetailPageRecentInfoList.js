import React from 'react';
import Card from './DetailPageRecentInfoListCard'
import './DetailPageRecentInfoList.css'

function RecentInfoList() {
    return(
        <div className="recentInfoList">
            <div>
                <span className="recentInfoListText">최신 뉴스</span>
            </div>
            <div className="recentListBox">
                <Card></Card>
                <Card></Card>
            </div>
        </div>
    );
}

export default RecentInfoList