import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFileImport } from '@fortawesome/free-solid-svg-icons';
import { nanoid } from 'nanoid';
import axios from 'axios';

import FileCard from '../FileCard/FileCard';
import './FileUpload.css';

const FileUpload = ({ handler }) => {
  const [files, setFiles] = useState([]);
  const [url, setUrl] = useState('');

  useEffect(() => {
    get_files()
  }, []);

  const get_files = () => {
    axios.get('http://127.0.0.1:5000/files')
      .then((response) => {
        setFiles(response.data);
        // console.log("get_files GET REQUEST ----> ", response);
      }, (error) => {
        console.log(error);
      });
  }

  const add_url = () => {
    // console.log(url);
    axios.put('http://127.0.0.1:5000/files', {
      type: 'url',
      url: url
    }).then((response) => {
      console.log("add_url REQUEST ----> ", response);
      if (response?.data?.success) {
        get_files()
      }
    }, (error) => {
      console.log(error)
    });
  }
  const handleOnclick = (e) => {
    e.preventDefault();
    e.stopPropagation();
  }

  const file_upload = () => {
    let file_upload = document.getElementById("file_upload");
    file_upload.click();
  }

  const on_file_change = (e) => {
    let files = Array.from(e.target.files);
    // console.log(files);
    files.map((file) => {
      let reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend = (e) => {
        axios.put('http://127.0.0.1:5000/files', {
          file_name: file.name,
          type: 'file',
          data_url: e.target.result.split(',')[1]
        }).then((response) => {
          // console.log("on_file_change PUT REQUEST ----> ", response);
          if (response?.data?.success) {
            get_files()
          }
        }, (error) => {
          console.log(error);
        });
      }
      return file;
    });
  }

  return (
    <div className="file_upload">
      <div className="user_input">
        <div className="input_field">
          <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} />
          <div className="clear_icon"></div>
          <div className="file_upload_icon" onClick={file_upload} >
            <input
              type="file"
              accept=".pdf, .txt, .docx"
              autoComplete="off"
              style={{ display: 'none' }}
              id="file_upload"
              onChange={on_file_change}
            />
            <FontAwesomeIcon icon={faFileImport} />
          </div>
        </div>
        <button onClick={add_url}>UPLOAD</button>
      </div>
      <div className="drop_area">
        <div className="cards">
          {files.map((file) => <FileCard key={nanoid()} name={file.name} info={file.info} ext={file.ext} handler={handler} />
          )}
        </div>
      </div>
    </div>
  );
};

export default FileUpload;