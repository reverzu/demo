import streamlit as st
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

if "run" not in st.session_state:
    st.session_state["run"] = False

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

        return img


if st.session_state["run"]:
    webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
    
button_yes = st.button("Start Streaming 📸")
button_no = st.button("Stop Streaming 📷")
if button_yes:
  st.session_state["run"] = True
if button_no:
  st.session_state["run"] = False
