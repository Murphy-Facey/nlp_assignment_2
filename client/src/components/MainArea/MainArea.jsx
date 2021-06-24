import { useEffect, useState } from "react";
import axios from 'axios';
import './MainArea.css';
// import ImageModal from "../ImageModal/ImageModal";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowCircleDown } from "@fortawesome/free-solid-svg-icons";
import { useSpeechSynthesis } from "react-speech-kit";
import { nanoid } from "nanoid";

const MainArea = ({ item, is_parse }) => {
  
  const [stopWords, setStopWords] = useState([]);
  const [tokens, setTokens] = useState([]);
  const [pos, setPos] = useState([]);
  const [rawText, setRawText] = useState("");
  const [optText, setOptText] = useState("");
  const [showText, setShowText] = useState(true);
  const [selectedToken, setSelectedToken] = useState({});
  // const [pageNums, setPageNums] = useState(0);

  const { speak, cancel } = useSpeechSynthesis();
  // const filename = nanoid();

  useEffect(() => {
    axios.put('http://127.0.0.1:5000/tokenize', { name: item })
      .then((response) => {
        console.log(response);
        const { tokens, pos, stop_words, raw_text, opt_text } = response.data;
        setPos(pos);
        setStopWords(stop_words);
        setTokens(tokens);
        setRawText(raw_text);
        setOptText(opt_text);
      }, (error) => {
        console.log(error);
      });
    
    
    window.addEventListener('beforeunload', cancel)
    return () => {
      window.removeEventListener('beforeunload', cancel)
    }
  }, []);

  const displayTokenInfo = (index) => {
    // console.log("TOKEN SELECTED ---->", tokens[index])
    setSelectedToken(tokens[index])
  }

  const show_panel = (elem) => {
    const items = ['.text_area', '.tokens_area', '.pos_and_sw'];
    const index = items.indexOf(elem);
    if(index > -1) { items.splice(index, 1); }

    document.querySelector(elem).classList.toggle('hide_panel');
    
    for (let i = 0; i < items.length; i++) {
      if(!document.querySelector(items[i]).classList.contains('hide_panel')) {
        document.querySelector(items[i]).classList.add("hide_panel");
      }
    }
  }

  const create_words = (word_list) => {
    var words = [];
    for(const [key, value] of Object.entries(word_list)) {
      words.push(<p key={nanoid()}>{key} <span className="index">{value}</span></p>);
    }
    return words;
  }

  const check_show_text = (is_showing) => {
    setShowText(is_showing);
    document.getElementById('optimized_text').checked = is_showing;
  }

  return (
    <div className="main_area_section">
      <button className="back" onClick={() => is_parse()}>Back to Main Menu</button>
      <div className="main_area_scrollable">
        <div className="text_area ">
          <div className="text_area_header ">
            <p>Text</p>
            <button onClick={() => speak({ text: optText })}>Start Reading</button>
            <button onClick={cancel}>Stop Reading</button>
            <div className="arrow_icon" onClick={() => show_panel('.text_area')}>
              <FontAwesomeIcon icon={faArrowCircleDown} />
            </div>
          </div>
          <div className="raw_text">
            <p>{showText ? optText : rawText}</p>
          </div>
          <div className="check_optimised">
            <input type="checkbox" id="optimized_text" name="optimised_text" onClick={() => setShowText(!showText)} defaultChecked={showText} />
            <p className="check_label" onClick={() => check_show_text(!showText)}>View Optimized Text</p>
          </div>
        </div>
        <div className="tokens_area hide_panel" >
          <div className="tokens_area_header">
            <p>Token</p>
            <p>Count: {tokens.length}</p>
            <div className="arrow_icon" onClick={() => show_panel('.tokens_area')}>
              <FontAwesomeIcon icon={faArrowCircleDown} />
            </div>
          </div>
          <div className="tokens_and_info ">
            <div className="tokens">
              <div className="tokens_scrollable">
              {tokens.map((token) => (
                <p key={nanoid()} onClick={() => displayTokenInfo(token.index)}>{token.text} <span className="index">{token.index}</span></p>
              ))}
              </div>
            </div>
            <div className="selected_token">
              <div className="token">
                <p>Selected Token</p>
                <p>{selectedToken.text}</p>
              </div>
              <div className="lemma">
                <p>Lemma</p>
                <p>{selectedToken.lemma}</p>
              </div>
              <div className="p_o_s">
                <p>Parts of Speech</p>
                <p>{selectedToken.pos}</p>
              </div>
              <div className="stop_word">
                <p>Shape</p>
                <p>{selectedToken.shape}</p>
              </div>
            </div>
          </div>
        </div>
        <div className="pos_and_sw hide_panel" >
          <div className="pos_and_sw_header">
            <p>Part of Speech & Stop Words</p>
            <div className="arrow_icon" onClick={() => show_panel('.pos_and_sw')}>
              <FontAwesomeIcon icon={faArrowCircleDown} />
            </div>
          </div>
          <div className="pos_sw">
            <div className="pos">
              <p className="pos_title">Part of Speech</p>
              <div className="pos_scrollable">
                <div className="part_of_speech">
                  {create_words(pos)}
                </div>
              </div>
            </div>
            <div className="sw">
              <p className="sw_title">Stop Words</p>
              <div className="sw_scrollable">
                <div className="stop_words">
                  {create_words(stopWords)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainArea;
