import { getThemeProps } from '@material-ui/styles';
import React from 'react';
import './InterestListCard.css'

function InterestListCard(props) {

    return(
        <div className="InterestListCard">
            <div className="InterestListCardCoin">
                <div className="InterestListCardIcon"></div>
                <div className="InterestListCardInfo">
                    <div className="InterestListCardCoinName">{props.name}</div>
                    <div className="InterestListCardCoinPrice">{props.price}</div>
                </div>
            </div>
            <div className="InterestListCardPricePerBox">
                <div className="InterestListCardPricePer">{props.pricerate}</div>
            </div>
        </div>
    );
}

export default InterestListCard