import React from "react";
// import waveHand from '../../assets/WAVING_HAND.gif';
import "./Header.css";

const Header = () => {
  return (
    <div className="header_section">
      <div className="welcome">
        {/* <img src={waveHand} alt="waving_hand.gif" /> */}
        <h3>Hello, welcome to</h3>
      </div>
      <div className="title">
        <h1>LIZ's Text To Speech</h1>
      </div>
    </div>
  );
};

export default Header;
