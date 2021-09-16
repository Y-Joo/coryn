import React, { Component, useState, useEffect } from "react";
import Chart from "react-apexcharts";

const axios = require('axios');

class ApexChart extends React.Component {

    constructor(props) {
        super(props);
        
    }

    render() {
        console.log(this.props);
        console.log(this.props.coin_price)
        console.log(this.props.coin_times)
        const item = this.props
        const coinPrice = this.props.coin_price
        const items = this.props.coin_times
        var ItemList = ''
        //분 시간 일 주
        if(Object.keys(this.props.coin_times).length !== 0 && Object.keys(this.props.coin_price).length !== 0){
            var price = {
                'open': this.props.coin_price.minute_open.split(','),
                'high': this.props.coin_price.minute_high.split(','),
                'low': this.props.coin_price.minute_low.split(','),
                'close': this.props.coin_price.minute_close.split(','),
            }
            ItemList = items && items.map((item, index) => ({  
                x: new Date(item.substr(0,19)),
                y: [ parseFloat(price.open[index]), parseFloat(price.high[index]), parseFloat(price.low[index]), parseFloat(price.close[index])] }
            )
            );
        }else{
            ItemList = []
        }  
        function a(item) {
            console.log(item)
            if(Object.keys(item.coin_times).length !== 0 && Object.keys(item.coin_price).length !== 0){
                var price = {
                    'open': item.coin_price.week_open.split(','),
                    'high': item.coin_price.week_high.split(','),
                    'low': item.coin_price.week_low.split(','),
                    'close': item.coin_price.week_close.split(','),
                }
                console.log(item.coin_price)
                ItemList = items && items.map((item, index) => ({  
                    x: new Date(item.substr(0,19)),
                    y: [ parseFloat(price.open[index]), parseFloat(price.high[index]), parseFloat(price.low[index]), parseFloat(price.close[index])] }
                )
                );
            }else{
                ItemList = []
            }
        }
        
        this.state = {
            itemList: [],
            series: [{
                data: ItemList
            }],
            options: {
                chart: {
                    type: 'candlestick',
                    height: 350,
                    toolbar:{
                        tools:{
                            customIcons: [{
                                icon: '주',
                                index: 2,
                                title: 'tooltip of the icon',
                                class: 'custom-icon',
                                click: function (chart, options, e) {
                                    console.log("clicked custom-icon")}
                            },
                            {
                                icon: '일',
                                index: 3,
                                title: 'tooltip of the icon',
                                class: 'custom-icon',
                                click: function (chart, options, e) {
                                  console.log("clicked custom-icon")
                                }
                            },
                            {
                                icon: '시',
                                index: 4,
                                title: 'tooltip of the icon',
                                class: 'custom-icon',
                                click: function (chart, options, e) {
                                  console.log("clicked custom-icon")
                                }
                            },
                            {
                                icon: '분',
                                index: 5,
                                title: 'tooltip of the icon',
                                class: 'custom-icon',
                                click: function (chart, options, e) {
                                  console.log("clicked custom-icon")
                                }
                            },
                        ]
                        }
                    },
                },
                title: {
                    text: this.props.coin_name,
                    align: 'left'
                },
                xaxis: {
                    type: 'datetime'
                },
                yaxis: {
                    tooltip: {
                        enabled: true
                    }
                }
            },

        };
        return (
            <div id="chart" style={{border:'1px solid black',width:'100vw'}}>
                <Chart options={this.state.options} series={this.state.series} type="candlestick" height={350} min-width={423} margin={0}/>
            </div>
        );
    }
}


export default ApexChart;