const Word = ({ text, number }) => {
  return (
    <div className="word">
      <p>{text}</p>
      <p className="number">{number}</p>
    </div>
  );
};

export default Word;
