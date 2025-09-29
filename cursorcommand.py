import cv2
import time
import os
import mediapipe as mp
import pyautogui
import numpy as np
from pynput.mouse import Controller, Button

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, 
                       min_tracking_confidence=0.5,
                       max_num_hands=1)

#Inisialisasi global
mp_drawing = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
smoothening = 5
prev_x, prev_y = 0, 0
last_click_time = 0
cooldown_duration = 1

pyautogui.FAILSAFE = False #Mac safety bypass

cooldown_duration = 0.5 #0.5 detik antar klik
last_action_time = {
    "left": 0,
    "right": 0,
    "double": 0,
    "screenshot": 0,
    "switch": 0  #KeyError
}

#Mouse controller
mouse = Controller()

def move_cursor(landmarks):
    global prev_x, prev_y
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    x = int(index_finger.x * screen_width)
    y = int(index_finger.y * screen_height)
    
    curr_x = prev_x + (x - prev_x) / smoothening
    curr_y = prev_y + (y - prev_y) / smoothening
    
    pyautogui.moveTo(curr_x, curr_y)
    prev_x, prev_y = curr_x, curr_y


def detect_clicks(landmarks):
    global last_action_time
    action = None
    
    #Landmark
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]

    #Knuckle 
    index_knuckle = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_knuckle = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_knuckle = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]
    pinky_knuckle = landmarks[mp_hands.HandLandmark.PINKY_MCP]

    #Jarak antar jari
    distance_index_thumb = np.linalg.norm([index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y])
    distance_middle_thumb = np.linalg.norm([middle_tip.x - thumb_tip.x, middle_tip.y - thumb_tip.y])
    distance_ring_thumb = np.linalg.norm([ring_tip.x - thumb_tip.x, ring_tip.y - thumb_tip.y])
    distance_pinky_thumb = np.linalg.norm([pinky_tip.x - thumb_tip.x, pinky_tip.y - thumb_tip.y])

    click_threshold = 0.07
    current_time = time.time()
    x, y = pyautogui.position()

    #Double click
    if distance_ring_thumb < click_threshold and (current_time - last_action_time["double"]) > 0.5:
        mouse.position = (x, y)
        mouse.click(Button.left, 2)
        last_action_time["double"] = current_time
        action = "Double Click"

    #Screenshot
    elif (thumb_tip.y < landmarks[mp_hands.HandLandmark.THUMB_IP].y and
          pinky_tip.y < pinky_knuckle.y and
          index_tip.y > index_knuckle.y and
          middle_tip.y > middle_knuckle.y and
          ring_tip.y > ring_knuckle.y and
          (current_time - last_action_time["screenshot"]) > 0.5):
        pyautogui.moveTo(x, y)
        time.sleep(0.9)
        pyautogui.hotkey('shift', 'command', '3')  # Screenshot di Mac
        last_action_time["screenshot"] = current_time
        action = "Screenshot triggered"

    #Left click
    elif distance_index_thumb < click_threshold and (current_time - last_action_time["left"]) > 0.5:
        pyautogui.click()
        last_action_time["left"] = current_time
        action = "Left Click"

    #Right click
    elif distance_middle_thumb < click_threshold and (current_time - last_action_time["right"]) > 0.5:
        pyautogui.rightClick()
        last_action_time["right"] = current_time
        action = "Right Click"

    #Switch Tab
    elif (index_tip.y < index_knuckle.y and
          middle_tip.y < middle_knuckle.y and
          ring_tip.y > ring_knuckle.y and
          pinky_tip.y > pinky_knuckle.y and
          (current_time - last_action_time["switch"]) > 1.0):
        pyautogui.hotkey("command", "tab")
        last_action_time["switch"] = current_time
        action = "Switch Window (Cmd+Tab)"

    return action

def handle_cursor_control(frame, results):
    action = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            #klik-kursor
            action = detect_clicks(landmarks)
            if action is None:
                move_cursor(landmarks)
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
    return action
