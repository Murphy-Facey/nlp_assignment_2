import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFilePdf, faCheckCircle, faFileWord, faFile, faFileCode } from "@fortawesome/free-solid-svg-icons";

import "./FileCard.css";

const FileCard = ({ name, info, ext, handler }) => {
  const handleOnclick = () => {
    ext !== 'url' ? 
    handler(name, true) : handler(info, true);
  };

  const select_icon = (ext) => {
    if(ext === 'url') return faFileCode;
    if(ext === '.docx') return faFileWord
    if(ext === '.pdf') return faFilePdf
    if(ext === '.txt') return faFile
  }

  return (
    <div className="file_card">
      <div className="file_icon_info">
        <FontAwesomeIcon
          icon={select_icon(ext)}
          size="2x"
          className="file_icon"
        />
        <div className="file_info">
          <div className="file_name">
            <p>Name: </p>
            <p>{name}</p>
          </div>
          <div className="size">
            <p>Size/URL: </p>
            <p>{info}</p>
          </div>
        </div>
      </div>
      <div className="present_icon">
        <FontAwesomeIcon icon={faCheckCircle} size="lg" color="yellowgreen" />
      </div>
      <button className="parse" onClick={handleOnclick}>
        Parse
      </button>
    </div>
  );
};

export default FileCard;
