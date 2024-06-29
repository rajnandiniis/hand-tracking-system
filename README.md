# Hand Tracking System

This repository contains the implementation of a Hand Tracking System using computer vision techniques and deep learning models. The system can detect and track hand movements in real-time using a webcam.

## Features

- Real-time hand detection and tracking
- Identification of hand landmarks (e.g., fingers, joints)
- Gesture recognition
- Easy integration with other applications

## Demo

![Hand Tracking Demo](demo.gif)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/rajnandiniis/hand-tracking-system.git
    cd hand-tracking-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the hand tracking system:**
    ```bash
    python hand_tracking.py
    ```

2. **Customize the system:**
   You can customize the hand tracking system by modifying the `config.json` file to adjust parameters such as detection confidence threshold, tracking confidence threshold, etc.

## Configuration

The configuration for the hand tracking system is located in the `config.json` file. Below is an example configuration:
```json
{
    "detection_confidence": 0.5,
    "tracking_confidence": 0.5,
    "max_num_hands": 2
}


Contact
If you have any questions or feedback, feel free to reach out to us at rajnandini1783@gmail.com.
