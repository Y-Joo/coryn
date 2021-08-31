import { React,useState, useEffect } from 'react';
import Card from './RecentInfoListCard'
import './RecentInfoList.css'

const axios = require('axios');


function RecentInfoList() {
    const [videoData, setVideoData] = useState([])
    useEffect(() => {
        axios.get(`/api/v1/coin/news/`)
            .then((response) => {
                console.log(response.data)
                setVideoData(response.data);
            }).catch((error) => {
                console.log(error);
                console.log(error);
            });
     }, [])
     //const date = videoData.upload_date.substring(0,18);
     //console.log(new Date(date));
    setVideoData.upload_date = Math.ceil((new Date() - new Date(videoData.upload_date))/(1000*3600*24));
    const items = videoData
    const ItemList = items && items.map((item) =>
    (
    <Card title={item.title ?? ''} upload_date={item.upload_date ?? ''}></Card>)
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