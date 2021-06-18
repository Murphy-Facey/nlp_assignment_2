import './App.css';
import Header from './components/Header/Header';
import FileUpload from './components/FileUpload/FileUpload';
import MainArea from './components/MainArea/MainArea';
import { useState } from 'react';

const App = () => {
  const [current, setCurrent] = useState('');
  const [isParse, setIsParse] = useState(false);

  const handler = (current, is_parse) => {
    setCurrent(current);
    setIsParse({isParse: is_parse});
  }

  return (
    <div className="App">
      <div className="main_area">
         <Header />
         {
           !isParse ? 
            <FileUpload handler={handler} />:
            <MainArea item={current} />
         }
      </div>
    </div>
  );
}

export default App;
