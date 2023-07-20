# AI - Attendance System - Emily Fletcher 18410839
import glob
# Project Title: AiAssignment2
# File Title: main.py
# File Purpose: Main Controller File, also contains the GUI
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
import os
import cv2
import tkinter as tk
import dateTime
from PIL import Image, ImageTk
import files
import lateChecker
import machineLearning
import saveFrame
from cameraFeed import detect_and_draw_faces

# Global Variables
videoPause = False
convertedTime = None
lateStatus = None
studentName = None
# Function that forgets current tab and loads the next.
def changeTab(tab):
    setUp.pack_forget()
    attendance.pack_forget()
    register.pack_forget()

    tab.pack()


# Register Attendance Button Action (3rd Tab)
def registerClicked():
    global convertedTime
    global studentName

    print("Register Clicked")
    # Parent Folder = sessions
    folder_path = "sessions"
    allSessions = os.listdir(folder_path)
    lastFile = None

    for currentFile in allSessions:
        if lastFile is None or currentFile > lastFile:
            lastFile = currentFile

    print("Last file in folder:", lastFile)

    time = dateTime.getCurrentTime()
    lateStatusCheck = lateChecker.check(time, convertedTime)
    lateStatus.config(text=lateStatusCheck)

    files.writeToFile(lastFile, lateStatusCheck, studentName)
    changeTab(attendance)


# Start Session Button Action (1st Tab)
# Gets Spinner Time and Converts to Time Object
# Creates Session Log
# Changes Tab to Attendance
def startButtonClick():
    global convertedTime
    # print("Start Button Clicked") Testing Print
    selectedTime = var.get()
    convertedTime = dateTime.getTime(selectedTime)
    files.createSessionLog(convertedTime)
    changeTab(attendance)


# Register Attendance Button Action (2nd Tab)
# Gets the Frame and saves it as a png
def buttonClick():
    global studentName
    # print("Button Clicked") Testing Print
    frame = fetchFrame.frame
    saveFrame.saveFrame(frame)
    image_path = "temp/frame.png"

    # If the image path exists open the image
    # (Used for the 3rd Tab)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        resized_image = image.resize((250, 200))
        photo = ImageTk.PhotoImage(resized_image)
        frameLabel.config(image=photo)
        frameLabel.image = photo

    studentName = machineLearning.frameSetup(frame)
    print("Predicted Student Name:", studentName)
    studentMatch.config(text=studentName, font=("Helvetica", 16, "bold"), padx=10, pady=10)

    changeTab(register)


# If cancelled, takes the user back to the 2nd Tab
def cancelButtonClicked():
    print("Cancel Button Clicked")
    changeTab(attendance)


# Create the Tkinter window
root = tk.Tk()
root.title("Attendance System")

# Frame Set Up
setUp = tk.Frame(root)
attendance = tk.Frame(root)
register = tk.Frame(root)

# Setting Application Window Dimensions
wWidth = 800
wHeight = 600
root.geometry(f"{wWidth}x{wHeight}")

# Tab Set One
descriptLabel = tk.Label(setUp, text="Select a Session Start Time and Press Button to Start Recording Attendance")
descriptLabel.pack()

spinnerLabel = tk.Label(setUp, text="Select Time")
spinnerLabel.pack()
spinnerValues = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
                 "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"]
var = tk.StringVar(value=spinnerValues[0])
dropdown = tk.OptionMenu(setUp, var, *spinnerValues)
dropdown.pack()

startButton = tk.Button(setUp, text="Start Session", command=startButtonClick)
startButton.pack()

# Tab Set Two
# Setting WebCam Dimensions
vWidth = int(wWidth * 0.8)
vHeight = int(wHeight * 0.8)

videoFrame = tk.Frame(attendance, width=vWidth, height=vHeight)
videoFrame.pack()

# Adding Video Frame and Labels to the App
videoSource = tk.Label(videoFrame)
videoSource.pack()

VSLabel = tk.Label(attendance, text="")
VSLabel.pack()

faceDetectionLabel = tk.Label(attendance)
faceDetectionLabel.pack()

button = tk.Button(attendance, text="Search for Student", command=buttonClick)
button.pack()
button.grid_remove()  # Hide the button initially

startSessionLabel = tk.Label(setUp, text="Start Session")
startSessionButton = tk.Label()

# Tab Set Three

# Setting Two Frames so Image is displayed side by side with the text values
savedFrame = tk.Label(register)
savedFrame.grid(row=0, column=0, padx=10, pady=10)
optionsFrame = tk.Frame(register)
optionsFrame.grid(row=0, column=1, padx=10, pady=10)

registerLabel = tk.Label(optionsFrame, text="If a Match is Found then Please Register Your Attendance")
registerLabel.pack()

frameLabel = tk.Label(savedFrame)
frameLabel.pack()

frameLabelText = tk.Label(savedFrame, text="Student Image")
frameLabelText.pack()

studentMatch = tk.Label(optionsFrame, text="No Match Found")
studentMatch.pack()

registerButton = tk.Button(optionsFrame, text="Register", command=registerClicked)
registerButton.pack()

timeRegistered = tk.Label(optionsFrame, text="Time Registered")
timeRegistered.pack()

lateStatus = tk.Label(optionsFrame, text="")
lateStatus.pack()

cancelButton = tk.Button(optionsFrame, text="Cancel Registration", command=cancelButtonClicked)
cancelButton.pack()


# Function to capture frames from the webcam and update GUI
def fetchFrame():
    if not videoPause:
        ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (vWidth, vHeight))
        frame_with_faces, labelStatus = detect_and_draw_faces(frame)
        image = Image.fromarray(frame_with_faces)
        photo = ImageTk.PhotoImage(image)
        videoSource.config(image=photo)
        videoSource.image = photo
        faceDetectionLabel.config(text=labelStatus)  # Update the label text

        fetchFrame.frame = frame

        # Only allows user to register attendance if there is a face in the frame
        if labelStatus == "Face Detected":
            button.pack()  # Show the button
        else:
            button.pack_forget()  # Hide the button

    # Schedule the next iteration of the capture_frame function after 10 milliseconds
    root.after(10, fetchFrame)


# Capture frames from webcam
video = cv2.VideoCapture(0)

fetchFrame()
# Ensure the correct tab is loaded when the application starts
changeTab(setUp)
root.mainloop()
