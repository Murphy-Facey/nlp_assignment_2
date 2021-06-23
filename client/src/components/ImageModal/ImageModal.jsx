import axios from "axios";
import { useEffect } from "react";
import "./ImageModal.css";

const ImageModal = () => {
  return (
  <div className="image_modal">
    <div className="image_container">
      <img src="http://127.0.0.1:5000/images" alt="" />
    </div>
    <div className="page_info">
      <button>Prev</button>
      <p><span>1</span> of <span>100</span></p>
      <button>Next</button>
    </div>
  </div>
  );
};
export default ImageModal;