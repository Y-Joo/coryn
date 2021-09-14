import React, { useState, useEffect } from 'react';
import Card from './InterestListCard'
import './InterestList.css'
import Divider from '@material-ui/core/Divider';
import { Link } from 'react-router-dom';

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
    (<li><Link to={"/detail/"+item.ticker}  style={{textDecoration:'none',color:'inherit'}}><Card name={item.coin_name ?? ''} price={item.coin_price[0].price ?? ''} pricerate={item.coin_price[0].day_change ?? ''} img={item.coin_img   ?? ''}></Card><Divider/></Link></li>
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
                </ul>
            </div>
        </div>
    );
}

export default InterestList