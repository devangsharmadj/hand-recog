# Hand Gesture Volume Control

This project allows you to control the volume of your computer by recognizing the distance between your index finger and thumb using OpenCV in Python. The application captures real-time video through your webcam, detects your hand, and adjusts the volume based on the distance between your index finger and thumb.

## Features

- Real-time hand detection using OpenCV.
- Volume control based on the distance between the index finger and thumb.
- Smooth and responsive volume adjustments.
- Visual feedback on the screen showing the detected hand and distance.

## Prerequisites

- Python 3.x
- OpenCV
- Mediapipe
- Pycaw

## How It Works

1. **Hand Detection**: The application uses Mediapipe to detect the hand landmarks in the video frame.

2. **Distance Calculation**: It calculates the Euclidean distance between the tips of the index finger and thumb.

3. **Volume Control**: The distance is mapped to a volume level using Pycaw, which interacts with the system's audio settings.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


