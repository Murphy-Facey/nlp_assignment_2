import { useEffect, useState } from "react";
import axios from 'axios';
 
import Tokens from "../Tokens/Tokens";
import Words from "../Words/Words";
import Speech from "../Speech/Speech";
import './MainArea.css';

const MainArea = ({ item }) => {
  const [stopWords, setStopWords] = useState([]);
  const [tokens, setTokens] = useState([]);
  const [pos, setPos] = useState([]);

  useEffect(() => {
    axios.put('http://127.0.0.1:5000/tokenize', { name: item })
      .then((response) => {
        console.log(response);
        const { tokens, pos, stop_words } = response.data;
        setPos(pos);
        setStopWords(stop_words);
        setTokens(tokens);
      }, (error)=> {
        console.log(error);
      });

      // axios.put('http://127.0.0.1:5000/parse', {file: item})
      //   .then((response) => {
      //     console.log(response);
      //   }, (error) => {
      //     console.log(error);
      //   })
  }, []);
  
  return (
    <div className="main_area_section">
      <div className="side_bar">
        <Words name="Parts of Speech" class_name="pos" word_list={pos} />
        <Words name="Stop Words" class_name="stop_words" word_list={stopWords} />
      </div>
      <div className="main_content">
        <div className="token_container">
          <div className="t_k">
            <Tokens name="Tokens" class_name="tokens" tokens={tokens} />
          </div>
          <div className="token_info">
            <p>No token selected</p>
          </div>
        </div>
        <div className="speech_area">
          <Speech file_name={item} />
        </div>
      </div>
    </div>
  );
};

export default MainArea;
