import React, { useState, useEffect } from 'react';import Card from './DetailPageRecentInfoListCard'
import './DetailPageRecentInfoList.css'

const axios = require('axios');

function RecentInfoList(props) {

    const items = props.videoData
    const ItemList = items && items.map((item) =>
    (<Card name={item.coin_name ?? ''} price={item.coin_price[0].price ?? ''} pricerate={item.coin_price[0].day_change ?? ''} img={item.coin_img   ?? ''}></Card>
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