# CSY3025 AS2 - AI Attendance Register
<img src="https://github.com/emilyf99UniversityProjects/CSY3025-AS2-AI-Attendance-Register/blob/main/A2.png?raw=true"> 

## Skills Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
## Introduction
This project was completed as Part of Year Three of BSC Software Engineering at the University of Northampton.

It was part of the module CSY3025 - Artificial Intelligence Techniques and was an assessment of the fundamentals of machine learning and AI with hands-on experience with AI-assisted applications.  

This project registers students' attendance within a timed session. It recognises the user against a trained model that was built by the author. 
It uses motion detection to detect if a user is in the frame, then a frame is captured and this is run against the model. 

When a face is detected, the image taken is cropped, this is to reduce false detection of other faces or background objects in the frame.

## Brief (Simplified)
Your task is to design and implement a deep-learning image classifier that can recognise students in the classroom from close-up facial images to register their attendance.

The classifier should have the capability of handling at least 5 (five) different people including yourself with a reasonable performance. Acquire other students’ permission if you wish to use photos of them for machine learning or testing. Other students’ identities should be anonymised. You should discuss your choice of performance metrics according to the application scenario. You are responsible for developing the image dataset for machine learning and testing. You must also critically analyse any bias and ethical challenges related to your dataset and model design. You are expected to design and implement additional features to achieve a higher grade. 

Examples of additional features are (but are not limited to): 
- Handling more people (>5)
- Handling multiple people in the same shot.
- Inclusion of different demographic groups,
- An exceptional performance demonstrated through “in-the-wild” testing
- Implementations of user interfaces/user applications


## Extra Images

### Face Detection with a bounding box 
<img src="https://github.com/emilyf99UniversityProjects/CSY3025-AS2-AI-Attendance-Register/blob/main/A2.png?raw=true"> 

### If there is no person detected, the user cannot progress
<img src="https://github.com/emilyf99UniversityProjects/CSY3025-AS2-AI-Attendance-Register/blob/main/A3.png?raw=true"> 

### Frame Captured and AI Person Detection
<img src="https://github.com/emilyf99UniversityProjects/CSY3025-AS2-AI-Attendance-Register/assets/72047699/9bb06699-fede-4342-9728-6a62f6b098b9"> 

### Text Log Generated
<img src="https://github.com/emilyf99UniversityProjects/CSY3025-AS2-AI-Attendance-Register/blob/main/A5.png?raw=true"> 
