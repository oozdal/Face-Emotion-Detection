import numpy as np
import streamlit as st
from deepface import DeepFace
from PIL import Image
from emotion import plot_emotion_probabilities
from streamlit_feedback import streamlit_feedback


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
    result = DeepFace.analyze(img_array, actions=['emotion'], 
                              enforce_detection=False)

    # Extract the dominant emotion
    dominant_emotion = result[0]['dominant_emotion']
    col2.write(f"Dominant Emotion: {dominant_emotion}")

    # Extract emotion probabilities
    emotion_probs = result[0]['emotion']
 
    # Plot the probabilities
    chart = plot_emotion_probabilities(emotion_probs)
    col2.altair_chart(chart, use_container_width=True)

    # Provide feedback using streamlit_feedback
    with col2.container(border=True):

        feedback_prompt = "We value your feedback! How was your experience today?"
        st.write(feedback_prompt)

        feedback = streamlit_feedback(feedback_type="faces",
                                optional_text_label="[Optional] Please provide an explanation", 
                                align="flex-start",
                                key='fb_k')
    
        if feedback:
            st.success("✔️ Thank you for your feedback!")
