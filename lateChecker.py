# AI - Attendance System - Emily Fletcher 18410839

# Project Title: AiAssignment2
# File Title: lateChecker.py
# File Purpose: Takes date objects and finds the difference, used to report if the student is late or on time.
# Author: Emily Fletcher
# Student Number: 18410839
# Version: 1.0

# Import Statements
from datetime import datetime, time


def check(currentTimeStr, convertedTimeStr):
    # Convert Time To AM/PM Layout
    convertedTime = datetime.strptime(convertedTimeStr, "%I:%M %p").time()
    print(convertedTime)
    # Convert Time to Hours Minute Layout
    currentTime = datetime.strptime(currentTimeStr, "%H:%M").time()
    print(currentTime)

    # Combine the times and subtract from each other to find difference
    timeDifference = datetime.combine(datetime.min, convertedTime) - datetime.combine(datetime.min, currentTime)
    print(timeDifference)
    # Statements account for 15 minute leeway if late or if the student is very early.
    if timeDifference.total_seconds() < -15 * 60:
        print("The student is early.")
        lateStatus = "The student is early"
    elif -15 * 60 <= timeDifference.total_seconds() <= 15 * 60:
        print("Registered On Time")
        lateStatus = "Registered On Time"
    else:
        print("The student is late.")
        lateStatus = "The student is late"
    return lateStatus

