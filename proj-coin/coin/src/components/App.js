import React, {Suspense} from 'react';
import Header from './configs/Header/Header';
import { Route, Switch } from 'react-router-dom';
//import LandingPage from './pages/LandingPage/LandingPage'
import InterestPage from './pages/InterestPage/InterestPage';
import DetailPage from './pages/DetailPage/DetailPage';
//import DetailPage from './pages/DetailPage/DetailPage'
import './App.css'
import BottomBar from '../components/configs/BottomBar/BottomBar'
import CalendarPage from './pages/CalendarPage/CalendarPage';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
  root: {
    display: 'flex',
    height: '100vh',
    width: '100vw',
    flexDirection: 'column',
    backgroundColor: 'rgb(243,242,246)',

  },
});

function App() {
  const classes = useStyles();
  return (
    <Suspense fallback={(<div>Loading...</div>)}>
        <div className={classes.root}>
        <Header></Header>
        <Switch>
          <Route exact path="/interest" component={InterestPage} />
          <Route exact path="/detail" component={DetailPage} />
          <Route exact path="/calendar" component={CalendarPage} />
        </Switch>
        <BottomBar/>
        </div>
    </Suspense>
  );
}

export default App;

//<Route exact path="/detail" component={DetailPage} />
//<Route exact path="/" component={LandingPage} />