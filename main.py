import streamlit as st
import cv2
button = st.button("This is a Button")
if button:
  st.text("Clicked")
  camera = cv2.VideoCapture(0)
  # Frame Window Initialiazation
  FRAME_WINDOW = st.image([])
