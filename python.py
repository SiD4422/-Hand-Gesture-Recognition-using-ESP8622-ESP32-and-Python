import cv2
import mediapipe as mp
import requests

ESP8266_IP = "http://192.168.137.115"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def control_led(path):
    url = f"{ESP8266_IP}{path}"
    try:
        response = requests.get(url, timeout=0.5)
        print(f"Sent: {path} | ESP8266: {response.text}")
    except Exception as e:
        print(f"Failed to send {path}: {e}")

def count_fingers(hand_landmarks):
    thumb_up = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < \
               hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    index_up = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < \
               hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_up = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < \
                hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_up = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < \
              hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_up = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < \
               hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    finger_status = [thumb_up, index_up, middle_up, ring_up, pinky_up]

    control_led("/led/thumb/on" if thumb_up else "/led/thumb/off")
    control_led("/led/index/on" if index_up else "/led/index/off")
    control_led("/led/middle/on" if middle_up else "/led/middle/off")
    control_led("/led/ring/on" if ring_up else "/led/ring/off")
    control_led("/led/pinky/on" if pinky_up else "/led/pinky/off")

    if not any(finger_status):
        print("All fingers are down")

    return finger_status

print("Starting camera...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW helps on Windows
print("cap.isOpened() =", cap.isOpened())

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = count_fingers(hand_landmarks)

    cv2.imshow('Hand Gesture Recognition', frame)

    if cv2.waitKey(5) & 0xFF == 27:  # Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
print("Finished.")
