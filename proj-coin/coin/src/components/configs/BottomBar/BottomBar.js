import React from 'react';
import { Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import BottomNavigation from './BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import RestoreIcon from '@material-ui/icons/Restore';
import FavoriteIcon from '@material-ui/icons/Favorite';
import LocationOnIcon from '@material-ui/icons/LocationOn';

const useStyles = makeStyles({
  root: {
    width: '100vw',
    height: '10vh',
    display: 'flex',
    justifyContent: 'center',
    backgroundColor: '#fff',
    position: 'fixed',
    bottom: '0px',
  },
  linkbox: {
    width: '33.33%',
  },
  button: {
    width: '100%',
    height: '100%',
    display: 'flex', 
    alignItems: 'center',
    justifyContent: 'center',
  }
});

export default function BottomBar() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);
  const [barNumber, setBarNumber] = React.useState(1);
  const selectedColor = 'aliceblue';
  const defaultColor = 'grey';
  
  const onclickHandler = (e) => {
    console.log(e)
    const index = e.target.id 
    console.log(index)
    setBarNumber(index)
  }

  const colorHandler = (index) => {
    console.log(index)
    if (index == barNumber) {
      return selectedColor
    } else {
      return defaultColor
    }
  }

  return (
    <div className={classes.root}>
      <Link to='/interest' className={classes.linkbox}><div id="1" className={classes.button} onClick={(e) =>onclickHandler(e)} style={{color:`${colorHandler(1)}`}}><RestoreIcon style={{height:'50%', width:'auto', pointerEvents:'none'}}/></div></Link>
      <Link to='/calendar' className={classes.linkbox}><div id="2" className={classes.button} onClick={(e) =>onclickHandler(e)} style={{color:`${colorHandler(2)}`}}><FavoriteIcon style={{height:'50%', width:'auto', pointerEvents:'none'}}/></div></Link>
      <Link to='/detail' className={classes.linkbox}><div id="3" className={classes.button} onClick={(e) =>onclickHandler(e)} style={{color:`${colorHandler(3)}`}}><LocationOnIcon style={{height:'50%', width:'auto', pointerEvents:'none'}}/></div></Link>
    </div>
    // <span>
    //   <BottomNavigation>
        
    //     <RestoreIcon />
    //     <FavoriteIcon />
    //     <LocationOnIcon />
    //     <BottomNavigationAction label="Recents" icon={<RestoreIcon />} />
    //     <BottomNavigationAction label="Favorites" icon={<FavoriteIcon />} />
    //     <BottomNavigationAction label="Nearby" icon={<LocationOnIcon />} />
    //   </BottomNavigation>
    // </span>
  );
}
