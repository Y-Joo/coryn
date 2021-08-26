import React from 'react';
import './DetailCard.css'

function InterestListCard() {
    return(
        <div className="root">
            <div className="coin">
                <div className="icon"></div>
                <div className="info">
                    <div className="coinname">비트코인</div>
                    <div className="coinprice">60000000</div>
                </div>
            </div>
            <div className="pricePerBox">
                <div className="pricePerInnerBox">
                    <div className="pricePer">+5.92%</div>
                    <div className="favorites">별</div>
                </div>
            </div>
        </div>
    );
}

export default InterestListCard