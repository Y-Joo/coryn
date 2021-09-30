import React, { useState, useEffect } from 'react';
import Card from './InterestListCard'
import './InterestList.css'
import Divider from '@material-ui/core/Divider';
import { Link } from 'react-router-dom';

const axios = require('axios');

function InterestList() {
    const [videoData, setVideoData] = useState([])
    const getPosts = async () => {
        axios.get(`/api/v1/coin/list/`)
            .then((response) => {
                //console.log(response.data)
                setVideoData(response.data);
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
    const [keyword,setKeyword] = useState([]);
    function searchSpace(event){
        setKeyword(event.target.value);
    }
    const items = videoData
    const ItemList = items && items.filter((item)=>{
        if(keyword == '')
            return item
        else if(item.coin_name.toLowerCase().includes(keyword.toLowerCase()) || item.kr_name.includes(keyword)){
            return item
    }}).map((item) =>
    (<li><Link to={"/detail/"+item.ticker}  style={{textDecoration:'none',color:'inherit'}}><Card name={item.kr_name ?? ''} ticker={item.ticker ?? ''} price={item.coin_price[0].price ?? ''} pricerate={item.coin_price[0].day_change ?? ''} img={item.coin_img   ?? ''}></Card><Divider/></Link></li>
    )
    );
    return (
        <span>
        <div style={{display:'flex',boxSizing:'border-box',margin: '0 1em',}}>
            <input type="text" class="form__field" placeholder="Search" onChange={(e)=>searchSpace(e)}/>
            <button>취소</button>
        </div>
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
        </span>
    );
}

export default InterestList