import React, { useState, useEffect } from 'react';import Card from './DetailPageRecentInfoListCard'
import './DetailPageRecentInfoList.css'

const axios = require('axios');

function RecentInfoList(props) {

    const items = props.newsData

    const ItemList = items && items.map((item) =>
    (<Card title={item.title ?? ''} link={item.link ?? ''} source={item.source ?? ''} upload_date={item.upload_date ?? ''} release_date={item.release_date ?? ''}></Card>
    )
    );
    return(
        <div className="recentInfoList">
            <div>
                <span className="recentInfoListText">최신 뉴스</span>
            </div>
            <div className="recentListBox">
                {ItemList}
            </div>
        </div>
    );
}

export default RecentInfoList