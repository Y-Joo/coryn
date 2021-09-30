import { getThemeProps } from '@material-ui/styles';
import React from 'react';
import './InterestListCard.css'

function InterestListCard(props) {
    var color = "InterestListCardPricePer_up";
    if(props.pricerate[0]=="-"){
        color = "InterestListCardPricePer_down";
    }
    var price = props.price;
    if(price>=100){
        price = price.substr(0,price.length-3);
    }
    return(
        <div className="InterestListCard">
            <div className="InterestListCardCoin">
                <div className="InterestListCardIcon"><img src={props.img}></img></div>
                <div className="InterestListCardInfo">
                    <div className="InterestListCardCoinName">
                        <div className="InterestListCardCoinName_en">{props.name}</div>
                        <div className="InterestListCardCoinName_ticker">{props.ticker}</div>
                    </div>
                    <div className="InterestListCardCoinPrice">{price}</div>
                </div>
            </div>
            <div className="InterestListCardPricePerBox">
                <div className={color}>{props.pricerate + '%'}</div>
            </div>
        </div>
    );
}

export default InterestListCard