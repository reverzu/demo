import streamlit as st
import cv2
# import mediapipe as mp
from streamlit_webrtc import WebRtcMode, webrtc_streamer

if "run" not in st.session_state:
    st.session_state["run"] = False


if st.session_state["run"]:
    # webrtc_streamer(key="key", desired_playing_state=True, video_processor_factory=EmotionProcessor)
    # webrtc_streamer(key="example", desired_playing_state=True)
    webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": get_ice_servers(),
        "iceTransportPolicy": "relay",
    },
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
    
button_yes = st.button("Start Streaming 📸")
button_no = st.button("Stop Streaming 📷")
if button_yes:
  st.session_state["run"] = True
if button_no:
  st.session_state["run"] = False

