import React from 'react';
import SearchBox from './SearchBox';
import RecentInfoList from './RecentInfoList';
import InterestList from './InterestList';

function InterestPage() {
    return(
        <div style={{backgroundColor:"rgb(243,242,246)",height:'80vh',overflow:'auto'}}>
            <SearchBox></SearchBox>
            <InterestList/>
            <RecentInfoList/>
        </div>
    );
}

export default InterestPage