import React from 'react';
import './SearchBox.css'

function SearchBox() {
  
    return(
      <div style={{display:'flex',boxSizing:'border-box',margin: '0 1em',}}>
        <input type="text" class="form__field" placeholder="Search"/>
        <button>취소</button>
      </div>
    );
}

export default SearchBox