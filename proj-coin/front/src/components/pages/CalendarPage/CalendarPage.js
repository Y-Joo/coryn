import React, { useState, useEffect } from 'react';
import { Calendar, Select, Button, Modal, Typography, Row, Col } from 'antd';
import './CalendarPage.css'
import "./antdCalendar.css";

const axios = require('axios');
const { Option } = Select;

function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

function CalendarPage() {
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [coinData, setcoinData] = useState();
    const [selectedKey, setSelectedKey] = useState(""); // 날짜
    const [isModalDetailVisible, setIsModalDetailVisible] = useState(false);
    const [selectedDetailKey, setSelectedDetailKey] = useState(""); // kr_coinname
    const [coinNameData, setCoinNameData] = useState({});
    const [selectedExchange, setSelectedExchange] = useState("upbit");

    useEffect(() => {
      axios.get('api/v1/coin/news/good/')
        .then((response) => {
          console.log(response.data)
          setcoinData(response.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }, [])
    var listData = coinData ?? '';

    function dateCellRender(value) {
      // console.log(coinData[tmpKey]);
      //console.log(upbitCoin);
      //const listData = coinData ?? '';
      var month=0;
      var date=0;
      if(Number(value.month())+1<10){
        month = '0'+(Number(value.month())+1);
      }
      else{
        month = (Number(value.month())+1);
      }
      if(value.date()<10){
        date = '0'+value.date();
      }
      else{
        date = value.date();
      }
      let tmpKey = value.year() + '-' + String(month) + '-' + date;
      const data = [];
      for(var i=0;i<listData.length;i++){
        var itemDate = listData[i].release_date.toString().substr(0,10)
        if(itemDate === tmpKey){
          for(var coin of listData[i].coins){
            data.push({coin_name: coin.coin_name, kr_name: coin.kr_name, ticker: coin.ticker, link: listData[i].link , realease_date: itemDate, title: listData[i].title})
          }
        }
      }
      const tickerdata = data.filter((item,pos)=>{
        var flag=0;
        for(var i=0;i<pos;i++){
          if(item.ticker == data[i].ticker)
            flag++;
        }
        if(flag==0) return item;
      }).map(item => (
          <li key={uuidv4()}>
            <span style={{fontSize: '0.6rem'}}>{item.ticker.split('-')[1]}</span>
          </li>
        ))

      return (
        <ul className="events">
          {tickerdata}
        </ul>
      );
    }

    const checkNameFromExchange = (exchange) => {

    }

    const modal = () => {
      // console.log(coinData);
      const data = [];
          for(var i=0;i<listData.length;i++){
            var itemDate = listData[i].release_date.toString().substr(0,10)
            if(itemDate === selectedKey){
              for(var coin of listData[i].coins){
                data.push({coin_name: coin.coin_name, kr_name: coin.kr_name, ticker: coin.ticker.split('-')[1], link: listData[i].link , realease_date: itemDate, title: listData[i].title})
              }
            }
          }

      // 모달이 이미 띄워져있는 경우
      if (isModalDetailVisible) {
        let newsData = []
        newsData = data && data.filter((item)=>{
          if(item.kr_name == selectedDetailKey){
            return item;
          }
        });

        return (
          <Modal 
              title={ selectedDetailKey + ' ' + newsData[0].coin_name + ' ' + '(' +newsData[0].ticker+ ')'}
              visible={isModalVisible} 
              onOk={handleOk}
              onCancel={handleCancel}
              footer={[
              <Button key="submit" type="primary" onClick={() => setIsModalDetailVisible(false)}>
                BACK
              </Button>,
              ]}>
            <ul className="modal" style={{overflow: 'auto', maxHeight: '10rem'}}>
              {newsData && newsData.map(item => (
                <li key={item.link} style={{marginBottom: '0.2rem'}}>
                  <a className="modal-content" href={item.link} target="_blank">{item.realease_date + ' ' + item.title}</a>
                </li>
              ))}
            </ul>
          </Modal>
        )
      } 
      // 모달이 처음 띄워지는 경우
      else {
          //let listData = coinData ?? null;
          const data2 = data && data.filter((item,pos)=>{        
              for(var i=0;i<pos;i++){
                if(data[i].ticker == item.ticker)
                  return;
              }
              return item
            }
            ).map(item => (
            <li key={uuidv4()} style={{marginBottom: '0.2rem'}}>
              <a className="modal-content" onClick={() => {setSelectedDetailKey(item.kr_name); setIsModalDetailVisible(true);}}>{item.kr_name +  ' (' + item.ticker + ')'}</a>
            </li>
          )) 
          if (listData !== ''){
            return (
              <Modal 
                  title={selectedKey}
                  visible={isModalVisible} 
                  onOk={handleOk}
                  onCancel={handleCancel}
                  footer={[
                  <Button key="submit" type="primary" onClick={handleOk}>
                    OK
                  </Button>,
                  ]}>
                <ul className="modal" style={{overflow: 'auto', maxHeight: '10rem'}}>
                  {data2}
                </ul>
              </Modal>
            )
          }
      }
    }

    const onClickCalendar = (value) => {
      var month=(Number(value.month())+1);
      var date=value.date();
      if(Number(value.month())+1<10){
        month = '0'+(Number(value.month())+1);
      }
      if(value.date()<10){
        date = '0'+value.date();
      }
      setSelectedKey(value.year() + '-' + String(month) + '-' + date);
      showModal();
    }

    const showModal = () => {
      setIsModalVisible(true);
    };
    
    const handleOk = () => {
      setIsModalVisible(false);
      setIsModalDetailVisible(false);
    };
    
    const handleCancel = () => {
      setIsModalVisible(false);
      setIsModalDetailVisible(false);
    };

    return (
      <div className='container'>
        {modal()}
          <Calendar 
            className="calendar" 
            dateCellRender={(value) => dateCellRender(value)} 
            onSelect={(value) => onClickCalendar(value)} 
            headerRender={({ value, type, onChange, onTypeChange }) => {
              const start = 0;
              const end = 12;
              const monthOptions = [];
      
              const current = value.clone();
              const localeData = value.localeData();
              const months = [];
              for (let i = 0; i < 12; i++) {
                current.month(i);
                months.push(localeData.monthsShort(current));
              }
      
              for (let index = start; index < end; index++) {
                monthOptions.push(
                  <Select.Option className="month-item" key={`${index}`}>
                    {months[index]}
                  </Select.Option>,
                );
              }
              const month = value.month();

              return (
                <div style={{ padding: 8 }}>
                  <Row gutter={8}>
                    <Col>
                      <Select
                        size="small"
                        dropdownMatchSelectWidth={false}
                        value={String(month)}
                        onChange={selectedMonth => {
                          const newValue = value.clone();
                          newValue.month(parseInt(selectedMonth, 10));
                          onChange(newValue);
                        }}
                      >
                        {monthOptions}
                      </Select>
                    </Col>
                  </Row>
                </div>
              );
            }}
            />
      </div>
    )
}

export default CalendarPage