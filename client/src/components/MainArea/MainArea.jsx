import { useEffect, useState } from "react";
import axios from 'axios';

import Tokens from "../Tokens/Tokens";
import Words from "../Words/Words";
import Speech from "../Speech/Speech";
import './MainArea.css';
import ImageModal from "../ImageModal/ImageModal";
import { nanoid } from "nanoid";

const MainArea = ({ item }) => {
  const [stopWords, setStopWords] = useState([]);
  const [tokens, setTokens] = useState([]);
  const [pos, setPos] = useState([]);
  const [rawText, setRawText] = useState("")
  const [selectedToken, setSelectedToken] = useState({})
  const [pageNums, setPageNums] = useState(0);

  const filename = nanoid();

  useEffect(() => {
    axios.put('http://127.0.0.1:5000/tokenize', { name: item })
      .then((response) => {
        console.log(response);
        const { tokens, pos, stop_words, raw_text } = response.data;
        setPos(pos);
        setStopWords(stop_words);
        setTokens(tokens);
        setRawText(raw_text);
      }, (error) => {
        console.log(error);
      });
    
    axios.put("http://127.0.0.1:5000/parse", { name: item, filename: filename })
      .then((response) => {
        console.log(response);
      }, (error) => {
        console.log(error);
      });
  }, []);

  const displayTokenInfo = (index) => {
    // console.log("INDEX SELECTED ---->", index)
    console.log("TOKEN SELECTED ---->", tokens[index])
    setSelectedToken(tokens[index])
  }

  return (
    <div className="main_area_section">
      {/* <ImageModal /> */}
      <div className="side_bar">
        <Words name="Parts of Speech" class_name="pos" word_list={pos} />
        <Words name="Stop Words" class_name="stop_words" word_list={stopWords} />
      </div>
      <div className="main_content">
        <div className="token_container">
          <div className="t_k">
            <Tokens name="Tokens" class_name="tokens" tokens={tokens} displayTokenInfo={displayTokenInfo} />
          </div>
          {selectedToken?.index > -1 ?
            <div className="token_info">
              <div>
                Token: <span style={{ marginLeft: "68px" }}>{selectedToken.text}</span>
              </div>
              <div>
                Lemma: <span style={{ marginLeft: "60px" }}>{selectedToken.lemma}</span>
              </div>
              <div>
                Part of speech: <span style={{ marginLeft: "18px" }}>{selectedToken.pos}</span>
              </div>
              <div>
                Stop words: <span style={{ marginLeft: "36px" }}>{selectedToken.is_stop_word ? "True" : "False"}</span>
              </div>
            </div>
            : null
          }
        </div>
        <div className="speech_area">
          <Speech speechText={rawText} />
        </div>
      </div>
    </div>
  );
};

export default MainArea;
