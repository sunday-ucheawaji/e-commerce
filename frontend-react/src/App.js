// import logo from './logo.svg';
import React from 'react';
import './styles/global.css';
import Navbar from './components/Navbar';
import Main from './components/Main';
import AdvertComponent from './components/AdvertComponent';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Main />
      <AdvertComponent />
    </div>
  );
}

export default App;
