import React from 'react';
import './DetailCard.css'

function InterestListCard(props) {
    return(
        <div className="root">
            <div className="coin">
                <div className="icon"><img src={props.img} style={{width:'100%', height:'100%'}}></img></div>
                <div className="info">
                    <div className="coinname">{props.name}</div>
                    <div className="coinprice">{props.price}</div>
                </div>
            </div>
            <div className="pricePerBox">
                <div className="pricePerInnerBox">
                    <div className="pricePer">{props.pricerate+'%'}</div>
                    {/* <div className="favorites">별</div> */}
                </div>
            </div>
        </div>
    );
}

export default InterestListCard