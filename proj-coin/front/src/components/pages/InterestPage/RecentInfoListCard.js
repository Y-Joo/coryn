import React from 'react';
import './RecentInfoListCard.css'


function RecentInfoListCard(props) {
    var triangle = "triangle_up";
    var RecentInfoListCardCoinRisingPrice = "RecentInfoListCardCoinRisingPrice_up";
    var RecentInfoListCardCoinRisingPriceRate = "RecentInfoListCardCoinRisingPriceRate_up";
    // if(props.daychange[0]=="-"){
    //     triangle = "triangle_down";
    //     RecentInfoListCardCoinRisingPrice = "RecentInfoListCardCoinRisingPrice_down";
    //     RecentInfoListCardCoinRisingPriceRate = "RecentInfoListCardCoinRisingPriceRate_down";
    // }
    return(
    <span>
    <a href={props.link} style={{color:'rgb(0,0,0)' ,textDecoration:'none'}}>
    <div className="RecentInfoListCard">
        {/* <div className="RecentInfoListCardInfo">
            <div className="RecentInfoListCardExchangeRate">
                {props.ticker}
            </div>
            <div className="RecentInfoListCardCoinName">
                {props.name}
            </div>
            <div className="RecentInfoListCardCoinPrice">
                {props.price}
            </div>
            <div className="RecentInfoListCardCoinPriceRate">
                <div className={triangle}></div>
                <div className={RecentInfoListCardCoinRisingPrice}>{props.daychange}</div>
                <div className={RecentInfoListCardCoinRisingPriceRate}>{props.daychange}</div>
            </div>
        </div> */}
        <div className="RecentInfoListCardNews">
            <div className="RecentInfoListCardTime">{props.upload_date.split('T')[0]+' | '+props.upload_date.split('T')[1].substr(0,8)}</div>
            <div className="RecentInfoListCardNewsTitle">{props.title}</div>
        </div>
    </div>
    </a>
    </span>
    );
}

export default RecentInfoListCard