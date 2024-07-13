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

**4. Feedback:**
After the predictions are shown, a feedback section will also appear as shown below. We value your input. Please share your experience with us!

![Screenshot 2024-07-01 at 10 54 43 PM](https://github.com/oozdal/Face-Emotion-Detection/assets/34719109/8771d43d-6927-44bc-90a3-8aefe0d3cc7c)

![Screenshot 2024-07-01 at 10 56 14 PM](https://github.com/oozdal/Face-Emotion-Detection/assets/34719109/2c459e5f-2213-4df3-aa51-7a38005799f0)

![Screenshot 2024-07-01 at 10 56 28 PM](https://github.com/oozdal/Face-Emotion-Detection/assets/34719109/bc7bb23f-0383-40ee-8933-a72682332aa3)

## PostgreSQL Database

We store the dominant emotion, timestamp, prediction probabilities and your feedback in the PostgreSQL database as shown below.

<img width="1411" alt="Screenshot 2024-07-13 at 7 09 07 PM" src="https://github.com/user-attachments/assets/b0e0c6f5-79c9-403c-9646-99796ae09949">

## Using Your Own PostgreSQL Database

If you would like to configure your own PostgreSQL database, follow these steps:

1. **Create Your PostgreSQL Database**
   - Set up a PostgreSQL database.
   - Create a table with the following columns:
     - `dominant_emotion` (type: STRING)
     - `timestamp` (type: STRING)
     - `prediction_probabilities` (type: JSON)

2. **Configure Your Environment**
   - Create a `.env` file.
   - Add the following line to the `.env` file:
     ```ini
     CONNECTION_URL=your_postgres_url_address
     ```
   - Replace `your_postgres_url_address` with the actual URL of your PostgreSQL database.

3. **Copy .env File into Docker Container**
   - Use the Docker copy command to copy the `.env` file into your Docker container:
     ```bash
     docker cp path/to/your/.env your_container_name:/path/inside/container/.env
     ```

4. **Run Your Application**
   - Start your Docker container if it isn't already running.
   - Your application should now be configured to use your PostgreSQL database.

