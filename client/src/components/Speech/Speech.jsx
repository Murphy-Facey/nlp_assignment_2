import { useEffect } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlay, faStop } from "@fortawesome/free-solid-svg-icons";
import { useSpeechSynthesis } from "react-speech-kit";


const Speech = ({ speechText }) => {
  const { speak, cancel, speaking } = useSpeechSynthesis();

  useEffect(() => {
    // console.log("LOAD-------->")
    window.addEventListener('beforeunload', cancel)
    return () => {
      window.removeEventListener('beforeunload', cancel)
    }
  })

  return (
    <div className="speech_container">
      <img src="" alt="" />

      {speechText.length > 0 ?
        <>
          <h3>Text to Speech</h3>
          <div className="media_icons">
            <div className="media_icon">
              {speaking ? (
                <FontAwesomeIcon icon={faStop} onClick={cancel} />
              ) : (
                <FontAwesomeIcon icon={faPlay} onClick={() => speak({ text: speechText })} />
              )}
            </div>
          </div>
        </>
        : null}
    </div>
  );
};


// const Speech = ({ file_name }) => {
//   const folder_name = nanoid();

//   const get_audio_file = (folder, index, file_name, should_play) => {
//     axios.post("http://127.0.0.1:5000/audios", {folder: folder, index: index, filename: file_name, play: should_play})
//       .then((response) => {
//         console.log(response.data);
//       }, (error) => {
//         console.log(error);
//       });
//   }

//   return (
//     <div className="speech_container">
//       <img src="" alt="" />
//       <h3>Text to Speech</h3>
//       <div className="media_icons">
//         <div className="media_icon">
//           <FontAwesomeIcon icon={faPlay} onClick={() => get_audio_file(folder_name, 0, file_name, 'play')}/>
//         </div>
//         <div className="media_icon" onClick={() => get_audio_file(folder_name, 0, file_name, 'stop')}>
//           <FontAwesomeIcon icon={faStop} />
//         </div>
//       </div>
//     </div>
//   );
// };

export default Speech;
