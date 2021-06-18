import React from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import './Home.css';

const Home = () => {
  // const [files, setFiles] = useState([]);
  // const [file, setFile] = useState('');

  const {acceptedFiles, getRootProps, getInputProps} = useDropzone({
    accept: ".pdf, .docx, .txt",
    onDrop: (acceptedFiles) => {
      acceptedFiles.map((file) => {
        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = (e) => {
          console.log(e.target.result.split(',').length)
          axios.put(
            "http://127.0.0.1:5000/files",
            {
              filename: file.name,
              dataUrl: e.target.result.split(',')[1]
            }
          ).then((response) => {
            console.log(response);
          }, (error) => {
            console.log(error);
          });
        }
        return file;
      });
    }
  });
  
  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  return(
    <div className="home_screen">
      <div className="top_area">
        <h1>Liz Text to Speech</h1>
      </div>
      <div className="bottom_area">
        <div className="input_area">
          {/* <input className="url_input" type="text" /> */}
          <input type="text" className="url_input" />
          <button>PROCESS</button>
        </div>
        <div {...getRootProps({className: "drop_area"})}>
          <input {...getInputProps()} />
          <p>Drop Files Here</p>
          <ul>{files}</ul>
          
        </div>
        <div>
          {/* <h4>Files</h4> */}
        </div>
      </div>
    </div>
  );
}

export default Home;