# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: dateTime.py
# File Purpose: Contains functions for setting times and dates
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
from datetime import datetime, date


# Receives time from spinner
# Converts it to a time that can be used in other functions
def getTime(time):
    # print("Selected Time:", time) Testing Statement
    timeConvert = datetime.strptime(time, "%H:%M")
    formattedTime = timeConvert.strftime("%I:%M %p")
    # print("Converted Time:", formattedTime) Testing Statement
    return formattedTime


# Gets the current date from the applications host machine
def getDate():
    currentDate = date.today()
    formattedDate = currentDate.strftime("%d-%m-%Y")
    # print("Formatted Date:", formattedDate) Testing Statement
    return formattedDate


def getCurrentTime():
    currentTime = datetime.now()
    formattedTime = currentTime.strftime("%H:%M")
    # print("Formatted Time:", formattedTime) Testing Statement
    return formattedTime
