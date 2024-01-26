# Hand Gesture Recognition using MediaPipe

![Hand Gesture Recognition](https://github.com/baukk/Gesture-Recognition/assets/76152244/52d33d2b-3cff-44c7-b504-a670c5927e67)

This Python project utilizes the [MediaPipe](https://mediapipe.dev/) library and [OpenCV](https://opencv.org/) to perform real-time hand gesture recognition. With this code, you can control your computer's cursor and keyboard using hand gestures.

## Features

- Detects and tracks hand landmarks in real time.
- Recognizes left and right-hand gestures for mouse and keyboard control.
- Control the mouse cursor and perform keyboard actions (e.g., move, click, swipe) using hand gestures.
- Easily customizable for different hand gestures and actions.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- PyAutoGUI (`pip install pyautogui`)

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/baukk/Gesture-Recognition.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Gesture-Recognition
   ```

3. Run the code:

   ```bash
   python main.py
   ```

4. A window will open showing the webcam feed. Move your hand in front of the camera to control the cursor and perform gestures.

5. To exit the program, press 'q' in the OpenCV window.

## Hand Gestures and Actions

- **Left Hand (Mouse Control):**
  - Move your left hand to control the mouse cursor.
  - When the index finger tip is above the index finger middle, it simulates a left mouse click.

- **Right Hand (Keyboard Control):**
  - Move your right hand to control the keyboard.
  - Swipe right or left to simulate arrow key presses ('right' or 'left').
  - Swipe up or down to simulate arrow key presses ('up' or 'down').

## Customization

You can customize this code to recognize additional hand gestures and map them to different actions. Modify the code to add your own gestures and actions.

## Acknowledgments

This project uses the [MediaPipe](https://mediapipe.dev/) library for hand landmark detection and tracking.

## License

This project is licensed under the MIT License.

## Author

- Tanay Gaur
- GitHub: [baukk](https://github.com/baukk)

Feel free to contribute to this project and make it even more awesome! If you have any questions or suggestions, please open an issue or pull request.

Enjoy controlling your computer with hand gestures! 🖐️🖥️
