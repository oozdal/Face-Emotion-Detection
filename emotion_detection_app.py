import streamlit as st

# Initialize the global variable
camera_photo = None
uploaded_photo = None

col1, col2 = st.columns([1, 2])

col1.markdown(" # Welcome to Face Emotion Detection App!")
col1.markdown(" Application iste amk neyini anlamiyon! ")

checkbox_val = col2.radio("Do you have a photo to upload or would you like to take a photo?", 
                          ("Take a photo", "Upload a photo"), index=0)

if checkbox_val == "Take a photo":
    camera_photo = col2.camera_input(" Take a photo")
    if camera_photo:
        col2.success(" Photo uploaded successfully!")

elif checkbox_val == "Upload a photo":
    uploaded_photo = col2.file_uploader(" Upload a photo", type=['png', 'jpeg', 'jpg'])
    if uploaded_photo:
        col2.image(uploaded_photo)
        col2.success(" Photo uploaded successfully!")

if uploaded_photo or camera_photo:
    col2.write("Emotion Detection")

