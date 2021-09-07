import React from 'react';
import Chart from './Chart';
import Card from './DetailCard';
import News from './DetailPageRecentInfoList'
import { useState, useEffect } from 'react';

const axios = require('axios');

function DetailPage({match}) {
    const [coinData, setCoinData] = useState({})
    const [coinPrice, setCoinPrice] = useState({})
    
    const coinId = match.params.videoId
    useEffect(() => {
        axios.get(`http://localhost:8000/api/v1/coin/detail/${coinId}/`)
            .then((response) => {
                console.log(response.data[0]);
                setCoinData(response.data[0]);
                setCoinPrice(response.data[0].coin_price[0]);
                console.log(coinPrice)
            }).catch((error) => {
                console.log(error);
            });
    }, [])
    return (
        <div style={{backgroundColor:"rgb(243,242,246)", width:'100vw', height:'80vh',overflow:'auto'}}>
            <Card name={coinData.coin_name ?? ''} img={coinData.coin_img ?? ''} price={coinPrice.price ?? ''} pricerate={coinPrice.day_change ?? ''}></Card>
            <Chart></Chart>
            <div>
                <News></News>
            </div>
        </div>
    );
}

export default DetailPage