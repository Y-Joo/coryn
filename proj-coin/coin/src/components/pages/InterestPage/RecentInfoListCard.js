import React from 'react';
import './RecentInfoListCard.css'


function RecentInfoListCard(props) {
    return(
    <div className="RecentInfoListCard">
        <div className="RecentInfoListCardInfo">
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
                <div className="triangle"></div>
                <div className="RecentInfoListCardCoinRisingPrice">{props.daychange}</div>
                <div className="RecentInfoListCardCoinRisingPriceRate">{props.daychange}</div>
            </div>
        </div>
        <div className="RecentInfoListCardNews">
            <div className="RecentInfoListCardTime">20분 전</div>
            <div className="RecentInfoListCardNewsTitle">{props.titie}</div>
        </div>
    </div>
    );
}

export default RecentInfoListCard