import streamlit as st
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

        return img



button = st.button("This is a Button")
if button:
  st.text("Clicked")
  webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
