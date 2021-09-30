import React from 'react';
import SearchBox from './SearchBox';
import RecentInfoList from './RecentInfoList';
import InterestList from './InterestList';
import Header from '../../configs/Header/Bar'
import '../../configs/Header/Bar.css'

function InterestPage() {
    return(
        <span>
        <Header>코인 목록</Header>
        <div style={{backgroundColor:"rgb(243,242,246)",height:'80vh',overflow:'auto'}}>

            <InterestList/>
            <RecentInfoList/>
        </div>
        </span>
    );
}

export default InterestPage