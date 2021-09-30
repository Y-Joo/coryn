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
    const [coinData, setcoinData] = useState({});
    const [selectedKey, setSelectedKey] = useState("");
    const [isModalDetailVisible, setIsModalDetailVisible] = useState(false);
    const [selectedDetailKey, setSelectedDetailKey] = useState("");
    const [coinNameData, setCoinNameData] = useState({});
    const [selectedExchange, setSelectedExchange] = useState("upbit");

    useEffect(() => {
      axios.get('api/v1/coin/news/good/')
        .then((response) => {
          console.log(response.data)
          setcoinData('');
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
      const data = listData 
      // && listData.map(item => (
      //   <li key={uuidv4()}>
      //     <span style={{fontSize: '0.6rem'}}>{item.coinSymbol}</span>
      //   </li>
      // ))
      return (
        <ul className="events">
          {data}
        </ul>
      );
    }

    const checkNameFromExchange = (exchange) => {

    }

    const modal = () => {
      // console.log(coinData);

      // 모달이 이미 띄워져있는 경우
      if (isModalDetailVisible) {
        //let listData = coinData ?? null;
          for (var keyDate in coinData) {
            if (selectedDetailKey in coinData[keyDate]) {
              for (var indx in coinData[keyDate][selectedDetailKey]) {
                let url = coinData[keyDate][selectedDetailKey][indx][0];
                let explain = coinData[keyDate][selectedDetailKey][indx][1]; 
                let fullName = coinData[keyDate][selectedDetailKey][indx][2]; 
                listData.push({date: keyDate, url: url, explain: explain, fullName: fullName});
              }
            } 
          }

        return (
          <Modal 
              title={ coinNameData[selectedExchange][selectedDetailKey] + " " + listData[0]['fullName'] + ' (' + selectedDetailKey + ')' }
              visible={isModalVisible} 
              onOk={handleOk}
              onCancel={handleCancel}
              footer={[
              <Button key="submit" type="primary" onClick={() => setIsModalDetailVisible(false)}>
                BACK
              </Button>,
              ]}>
            <ul className="modal" style={{overflow: 'auto', maxHeight: '10rem'}}>
              {listData && listData.map(item => (
                <li key={item.url} style={{marginBottom: '0.2rem'}}>
                  <a className="modal-content" href={item.url} target="_blank">{item.date + " " + item.explain}</a>
                </li>
              ))}
            </ul>
          </Modal>
        )
      } 
      // 모달이 처음 띄워지는 경우
      else {
          //let listData = coinData ?? null;
          const data2 = listData 
          // && listData.map(item => (
          //   <li key={uuidv4()} style={{marginBottom: '0.2rem'}}>
          //     <a className="modal-content" onClick={() => {setSelectedDetailKey(item.coinSymbol); setIsModalDetailVisible(true);}}>{item.coinKoreanName +  ' (' + item.coinSymbol + ')'}</a>
          //   </li>
          // )) 
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
      setSelectedKey(value.year() + '/' + String(Number(value.month())+1) + '/' + value.date());
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