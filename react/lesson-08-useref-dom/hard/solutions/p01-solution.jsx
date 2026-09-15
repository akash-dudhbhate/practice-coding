// Lesson 08 — Hard P01: VideoPlayer
import { useRef, useState } from "react";
function VideoPlayer() {
  const videoRef = useRef(null);
  const [playing, setPlaying] = useState(false);
  const togglePlay = () => {
    const v = videoRef.current;
    if (playing) { v.pause(); } else { v.play(); }
    setPlaying(!playing);
  };
  const seek = (time) => { videoRef.current.currentTime = time; };
  return (
    <div>
      <video ref={videoRef} src="https://www.w3schools.com/html/mov_bbb.mp4" width="400" controls />
      <div>
        <button onClick={togglePlay}>{playing ? "Pause" : "Play"}</button>
        <button onClick={() => seek(0)}>Restart</button>
        <button onClick={() => seek(videoRef.current.currentTime + 10)}>+10s</button>
      </div>
    </div>
  );
}
export default VideoPlayer;
