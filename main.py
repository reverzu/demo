import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer

button = st.button("This is a Button")
if button:
  st.text("Clicked")
  webrtc_streamer(key="example")
