# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: cameraFeed.py
# File Purpose: Loads camera frames as well as assigns computer vision techniques
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
import cv2

# Load Face Recognition From Open CV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Global variables
labelStatus = "No Face Detected"


def detect_and_draw_faces(frame):
    # Fetch Global Label
    global labelStatus

    # Changing the frame to Grey Scale, Makes Face Recognition Easier
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a face has been detected, update global label
    if len(faces) > 0:
        labelStatus = "Face Detected"
    else:
        labelStatus = "No Face Detected"

    # Code to Draw a Green Box around any faces found
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Returning the current video frame
    # Returns if a face has been detected
    # Returns Face Boolean
    return frame, labelStatus