import React, { useState, useEffect } from 'react';
import Card from './InterestListCard'
import './InterestList.css'
import Divider from '@material-ui/core/Divider';

const axios = require('axios');

function InterestList() {
    const [videoData, setVideoData] = useState([])
    useEffect(() => {
        axios.get(`http://54.180.16.31:5000/api/v1/coin/`)
            .then((response) => {
                console.log(response)
                setVideoData(response.data.data);
            }).catch((error) => {
                console.log(error);
            });
     }, [])
    const items = videoData
    const ItemList = items && items .map((item) =>
    (<li><Card name={item.coin.name ?? ''} price={item.coin_price.price ?? ''} pricerate={item.coin_price.daychange ?? ''}></Card><Divider/></li>
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