import React from 'react';
import Chart from './Chart';
import Card from './DetailCard';
import News from './DetailPageRecentInfoList'


function DetailPage() {
    return (
        <div style={{backgroundColor:"rgb(243,242,246)", width:'100vw', height:'80vh',overflow:'auto'}}>
            <Card></Card>
            <Chart></Chart>
            <div>
                <News></News>
            </div>
        </div>
    );
}

export default DetailPage