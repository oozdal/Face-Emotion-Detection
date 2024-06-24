# Use the official DeepFace image as a base
FROM serengil/deepface

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Expose the port Streamlit is running on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "emotion_detection_app.py", "--server.port=8501"]