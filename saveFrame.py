# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: saveFrame.py
# File Purpose: Controls the current frames and saving them as PNGS
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
import os
import cv2

from cameraFeed import face_cascade


# Saves the current frame as a PNG
def saveFrame(frame):
    # Create a folder if it does not exist.
    folder_name = "temp"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        cropped_frame = frame[y:y + h, x:x + w]
    else:
        cropped_frame = frame

    # Save the cropped frame as an image in the folder
    file_name = os.path.join(folder_name, "frame.png")
    # Converts the frame to a colour frame for ease of use
    # Originally greyscale to help computer vision
    cv2.imwrite(file_name, cv2.cvtColor(cropped_frame, cv2.COLOR_RGB2BGR))

    # print("Frame saved successfully!") Test Statements

# Deletes the frames in the folder
# Not currently used
def deleteFrame():
    # Specify the folder to be cleared
    folder_name = "temp"

    # Check if the folder exists
    if os.path.exists(folder_name):
        # Get a list of all files in the folder
        file_list = os.listdir(folder_name)

        # Delete each file in the folder
        for file in file_list:
            file_path = os.path.join(folder_name, file)
            os.remove(file_path)

        print("Folder cleared")
    else:
        print("Folder does not exist.")
