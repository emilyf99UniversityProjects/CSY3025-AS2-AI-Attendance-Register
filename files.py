# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: files.py
# File Purpose: Creates the Session Log and Parent Folder
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
import os
import dateTime


def createSessionLog(time):
    # Create Folder if it does not exist
    folder_name = "sessions"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # print("Folder Created") Testing Statement

    # Getting date values for the session
    todaysDate = dateTime.getDate()

    # : causes issues with the file name, so replaced with underscore
    time = time.replace(":", "_")

    fileName = "Session_Date_" + todaysDate + "_Session_Time_" + time + ".txt"
    filePath = os.path.join(folder_name, fileName)
    startingText = "Start of Attendance Log\n"

    # Writes the starting text and marks the file as readable
    with open(filePath, "w") as file:
        file.write(startingText)

    # Used to edit and save to a file
def writeToFile(fileName, fileContent, studentName, folderPath = "sessions"):
    if folderPath:
        fileName = os.path.join(folderPath, fileName)
    totalContent = "Student: " + studentName + " Late Status: " + fileContent + "\n"
    with open(fileName, 'a') as file:
        file.write(totalContent)
