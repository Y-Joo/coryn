import React, { useState, useEffect } from 'react';
import Card from './InterestListCard'
import './InterestList.css'
import Divider from '@material-ui/core/Divider';

const axios = require('axios');

function InterestList() {
    const [videoData, setVideoData] = useState([])
    useEffect(() => {
        axios.get(`/api/v1/coin/list/`)
            .then((response) => {
                console.log(response.data)
                setVideoData(response.data);
            }).catch((error) => {
                console.log(error);
            });
     }, [])
    const items = videoData
    const ItemList = items && items.map((item) =>
    (<li><Card name={item.coin_name ?? ''} price={item.coin_price[0].price ?? ''} pricerate={item.coin_price[0].day_change + '%' ?? ''}></Card><Divider/></li>
    )
    );
    return (
        <div className="interestList">
            <div>
                <span className="interestListText">관심목록</span>
            </div>
            <div className="interestListBox">
                <ul>
                    {ItemList}
                    <li><Card></Card></li>
                </ul>
            </div>
        </div>
    );
}

export default InterestList