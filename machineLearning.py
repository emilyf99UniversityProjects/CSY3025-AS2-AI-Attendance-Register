# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: machineLearning.py
# File Purpose: Connects to the model and inserts the frame into the model
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
import cv2

from tensorflow import keras

import os
import shutil

# from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow import keras
# from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# from google.colab import drive
# from google.colab import files

# Load the saved model
model_dir = "model"
model_file = "model.h5"
model_path = os.path.join(model_dir, model_file)
# Check if the model file exists
if os.path.exists(model_path):
    try:
        # Load the model from the file
        model = keras.models.load_model(model_path)
    except Exception as e:
        print("Error loading the model")
else:
    print("Model file not found!")


def frameSetup(frame):
    # Preprocess the frame (resize, normalize, etc.) to match the model's requirements
    resizeFrame = cv2.resize(frame, (180, 180))
    resizeFrame = resizeFrame / 255.0  # Normalize the pixel values
    resizeFrame = np.expand_dims(resizeFrame, axis=0)

    print("Frame Processed")

    # List of Students
    students = {
        0: "Alpha",
        1: "Bravo",
        2: "Charlie",
        3: "Delta",
        4: "Echo"
    }
    prediction = model.predict(resizeFrame)
    predicted = np.argmax(prediction)
    # Map the predicted class to a student name using the class_mapping dictionary
    student_found = students.get(predicted, "Unknown")
    print("Prediction Weights:", prediction)
    print("Predicted student:", student_found)
    return student_found
