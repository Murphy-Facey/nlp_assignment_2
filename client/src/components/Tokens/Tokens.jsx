import { nanoid } from "nanoid";
import Word from "../Word/Word";

const Tokens = ({ tokens, class_name, name, displayTokenInfo }) => {

  return (
    <div className={class_name}>
      <h3>{name}</h3>
      <div className="words">
        {tokens.map((token) => (
          <div key={nanoid()} onClick={() => displayTokenInfo(token.index)}>
            <Word text={token.text} number={token.index} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Tokens;