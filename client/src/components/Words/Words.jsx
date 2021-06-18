import { nanoid } from "nanoid";

import Word from "../Word/Word";
import './Words.css';

const Words = ({ name, class_name, word_list }) => {
  
  var words = [];
  const create_words = () => {
    for(const [key, value] of Object.entries(word_list)) {
      words.push(<Word key={nanoid()} text={key} number={value}/>);
      // console.log(key + ' ' + value);
    }
    return words;
  }
  
  return (
    <div className={class_name}>
      <h3>{name}</h3>
      <div className="words">
        {create_words()}
      </div>
    </div>
  );
};

export default Words;
