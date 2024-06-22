# Volume Control with Your Index Finger 🎛️👆

https://github.com/fastuptime/Volume_Up_And_Down_With_Your_Index_Finger/assets/63351166/2ae097b3-68be-4f27-b5b1-7680b6a49d5d

## Overview 🌟

Welcome to the **Volume Control with Your Index Finger** repository! This project uses OpenCV and MediaPipe to control your computer's volume with simple hand gestures. Move your index finger to the right to increase the volume and to the left to decrease it. 

## Features 🚀

- **Real-Time Hand Gesture Recognition**: Control volume with your index finger in real-time.
- **Simple User Interface**: Clear visual cues for volume control actions.
- **Easy to Use**: No need for additional hardware, just your webcam.

## Installation and Setup 🛠️

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/fastuptime/Volume_Up_And_Down_With_Your_Index_Finger.git
   cd Volume_Up_And_Down_With_Your_Index_Finger
   ```

2. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install required packages:
     ```sh
     pip install opencv-python mediapipe numpy pyautogui
     ```

3. **Run the Program**:
   - Execute the Python script:
     ```sh
     python volume_control.py
     ```

## Usage 💻

1. **Launch the Program**:
   - Run the script. The webcam will start, and the program will begin detecting hand gestures.

2. **Volume Control**:
   - Move your index finger to the right to increase the volume.
   - Move your index finger to the left to decrease the volume.
   - Visual cues will be displayed on the screen indicating the current action.

3. **Exit the Program**:
   - Press the 'Esc' key to quit the program.

## Code Explanation 📝

### `volume_control.py`

- **Import Libraries**:
  ```python
  import cv2
  import mediapipe as mp
  import numpy as np
  import pyautogui
  ```

- **Initialize MediaPipe and OpenCV**:
  ```python
  mp_drawing = mp.solutions.drawing_utils
  mp_hands = mp.solutions.hands

  cap = cv2.VideoCapture(0)
  ```

- **Volume Control Function**:
  ```python
  def volume_control():
      with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
          while cap.isOpened():
              success, image = cap.read()
              if not success:
                  print("Kamera açılamadı. Yazılım kapatılıyor.")
                  continue

              image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
              image.flags.writeable = False
              results = hands.process(image)

              image.flags.writeable = True
              image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

              if results.multi_hand_landmarks:
                  for hand_landmarks in results.multi_hand_landmarks:
                      mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                      x = hand_landmarks.landmark[8].x
                      y = hand_landmarks.landmark[8].y
                      cv2.circle(image, (int(x*640), int(y*480)), 5, (255, 0, 0), -1)
                      cv2.putText(image, '< Azalt / Artir >', (int(x*640), int(y*480)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                      
                      if x > 0.5:
                          cv2.putText(image, 'Sesi Artir', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                          pyautogui.press('volumeup')
                      else:
                          cv2.putText(image, 'Sesi Azalt', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                          pyautogui.press('volumedown')

              cv2.imshow('Ses Kontrol', image)
              if cv2.waitKey(5) & 0xFF == 27:
                  break

  volume_control()
  cap.release()
  cv2.destroyAllWindows()
  ```

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
