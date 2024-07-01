# Face-Emotion-Detection

This repository contains a Streamlit application designed to predict facial emotions from both uploaded images and pictures taken directly with the camera. Users can either upload an existing image or use their device's camera to capture a new one, and the application will analyze the facial features to determine the displayed emotion.

## Usage, Deployment & Streamlit User Interface

The application is deployed and accessible via Railway: [Face Emotion Detection App](https://face-emotion-detection-production.up.railway.app/) and [DockerHub](https://hub.docker.com/r/ozerozdal/emotion-detection-app)


## Screenshots

![Screenshot 2024-07-01 at 4 48 19 PM](https://github.com/oozdal/Face-Emotion-Detection/assets/34719109/cf629d76-c2c6-41df-b047-069a9bcebf82)

<img width="1427" alt="Screenshot 2024-07-01 at 4 50 02 PM" src="https://github.com/oozdal/Face-Emotion-Detection/assets/34719109/3ea5491a-e6e1-4204-9a13-06be12afde1a">

## Features

**Take Your Own Picture**: Use your camera to take a picture within the application.

**Upload Images**: Users can upload images directly through the Streamlit interface.

**Emotion Prediction**: The application analyzes the uploaded images and predicts the emotions of the faces in the images.

**Interactive Interface**: Built with Streamlit, the application provides an interactive and user-friendly interface.

## How to Run

To run the application locally using Docker, follow these steps:

**1. Pull the Docker Image**

```bash
docker pull ozerozdal/emotion-detection-app:latest
```


**2. Run the Docker Container**

```docker
docker run -p 8501:8501 ozerozdal/emotion-detection-app:latest
```

**3. Access the Application**

Open your web browser and go to http://localhost:8501 to access the Streamlit application.

## Usage

**1. Launch the Application**:
Open the application in your web browser.

**2. Provide Access:**
Allow the application to access your camera, then either take a picture or upload an image by clicking the "Upload" button or dragging and dropping an image.

**3. View Results:**
Wait for the model to process the image and display the predicted emotion.

## Development

If you want to develop this application further, follow these steps:

**1. Clone the Repository**

```bash
git clone https://github.com/oozdal/Face-Emotion-Detection.git
cd Face-Emotion-Detection
```

**2. Set Up a Virtual Environment***

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Application Locally**

```bash
streamlit run emotion_detection_app.py --server.port 8501
```

**5. Access the Application**

Open your web browser and go to http://localhost:8501 to access the Streamlit application.

**6. Make Changes**

You can now make changes to the application. The main script is emotion_detection_app.py, and you can modify the model, UI, or other components as needed.
