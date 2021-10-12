import React from 'react';
import Chart from './Chart';
import Card from './DetailCard';
import News from './DetailPageRecentInfoList'
import { useState, useEffect } from 'react';
import Header from '../../configs/Header/Bar'
import back from './back2.svg'

const axios = require('axios');

function DetailPage({match,history}) {
    const [coinData, setCoinData] = useState({})
    const [coinPrice, setCoinPrice] = useState({})
    //const [time,setTime] = useState(0)
    const goBack = () => {
        history.goBack();
      };
    const coinId = match.params.videoId
    const getPosts = async () => {
            axios.get(`http://localhost:8000/api/v1/coin/detail/${coinId}/`)
            .then((response) => {
                //console.log(response.data[0]);
                //console.log(time);
                setCoinData(response.data[0]);
                setCoinPrice(response.data[0].coin_price[0]);
                //console.log(coinPrice)
            }).catch((error) => {
                console.log(error);
            });
    }
    useEffect(() => {
        getPosts()
        const interval=setInterval(()=>{
                getPosts()
                },5000)
                
                
        return()=>clearInterval(interval)
    }, [])
    //setInterval(function (){setTime(time+1)},60);
    return (
    <span>
        <Header style={{paddingLeft:0}}><div onClick={goBack}><img src={back}></img></div>코인 정보</Header>
        <div style={{backgroundColor:"rgb(243,242,246)", width:'100vw', height:'82vh',overflow:'auto'}}>
            <Card name={coinData.coin_name ?? ''} img={coinData.coin_img ?? ''} price={coinPrice.price ?? ''} pricerate={coinPrice.day_change ?? ''}></Card>
            <Chart coin_price={coinPrice ?? ''} coin_times={coinData.times ?? ''}></Chart>
            <div>
                <News newsData={coinData.coin_newses}></News>
            </div>
        </div>
    </span>
    );
}

export default DetailPage