import cv2
import mediapipe as mp
import numpy as np
import time
import keyboard
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

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
