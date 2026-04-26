# GestureVision

## Overview

This project implements a **real-time hand gesture recognition system** that detects and counts the number of fingers using a webcam. It leverages **MediaPipe Hands** for landmark detection.      and **OpenCV** for video processing.


## Features

* Real-time hand tracking using webcam
* Identifies **Left / Right hand**
* Counts number of fingers raised
* Simple and efficient implementation


## Tech Stack

* Python
* OpenCV
* MediaPipe

## System Design

The system is a real-time hand gesture recognition pipeline that captures video input, processes frames, detects hand landmarks, and outputs the number of fingers displayed.

 ## Workflow
Camera Input → Frame Capture → Preprocessing → Hand Detection → Landmark Extractio

## How It Works

* Captures video using OpenCV
* Converts frame to RGB
* Uses MediaPipe to detect hand landmarks
* Compares finger tip and joint positions
* Displays finger count on screen


## Requirements

* Python 3.7 – 3.11
* Webcam
* Minimum 4GB RAM


## Future Improvements

* Add gesture-based controls (volume, brightness)
* Integrate with AI models for gesture classification
* Build GUI using Tkinter or PyQt
* Deploy as a web app

## Conclusion

This project demonstrates a real-time hand gesture recognition system using computer vision techniques.The implementation highlights how rule-based logic can be used to solve gesture recognition problems without requiring complex machine learning models, making it lightweight and suitable for real-time applications.

