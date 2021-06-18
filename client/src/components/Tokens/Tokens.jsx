import { nanoid } from "nanoid";
import Word from "../Word/Word";

const Tokens = ({ tokens, class_name, name }) => {
  return (
    <div className={class_name}>
      <h3>{name}</h3>
      <div className="words">
        {tokens.map((token) => (
          <Word key={nanoid()} text={token.text} number={token.index} />
        ))}
      </div>
    </div>
  );
};

export default Tokens;