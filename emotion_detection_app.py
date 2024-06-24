import numpy as np
import streamlit as st
from deepface import DeepFace
from PIL import Image


# Initialize the global variable
uploaded_photo = None

col1, col2 = st.columns([1, 2])

col1.markdown(" # Welcome to Face Emotion Detection App!")

checkbox_val = col2.radio("Do you have a photo to upload or would you like to take a photo?", 
                          ("Take a photo", "Upload a photo"), index=0)

if checkbox_val == "Take a photo":
    uploaded_photo = col2.camera_input(" Take a photo")
    if uploaded_photo:
        col2.success(" Photo uploaded successfully!")

elif checkbox_val == "Upload a photo":
    uploaded_photo = col2.file_uploader(" Upload a photo", type=['png', 'jpeg', 'jpg'])
    if uploaded_photo:
        col2.image(uploaded_photo)
        col2.success(" Photo uploaded successfully!")

if uploaded_photo:

    # Open the uploaded image
    image = Image.open(uploaded_photo)

    # Convert image to numpy array
    img_array = np.array(image)

    # Analyze the image using DeepFace
    result = DeepFace.analyze(img_array, actions=['age', 'gender', 'race', 'emotion'], 
                              enforce_detection=False)

    # Extract the predicted age
    age = result[0]['age']
    col2.write(f"Predicted Age: {age}")

    # Extract the dominant gender
    dominant_gender = result[0]['dominant_gender']
    col2.write(f"Dominant Gender: {dominant_gender}")

    # Extract the dominant race
    dominant_race = result[0]['dominant_race']
    col2.write(f"Dominant Race: {dominant_race}")

    # Extract the dominant emotion
    dominant_emotion = result[0]['dominant_emotion']
    col2.write(f"Dominant Emotion: {dominant_emotion}")

