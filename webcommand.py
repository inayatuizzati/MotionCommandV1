import cv2
import pyautogui
import time
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

#Teks
gesture_actions = {
    "swipe_left": "Go to Previous Tab",
    "swipe_right": "Go to Next Tab",
    "scroll_up": "Page Scroll Up",
    "scroll_down": "Page Scroll Down",
    "open_tab": "Create New Tab",
    "close_tab": "Close Current Tab",
    "refresh": "Reload Page",
    "play_pause": "Toggle Play/Pause",
}

last_action_time = time.time()
cooldown_time = 1.5

def get_finger_status(landmarks):
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]
    thumb_tip = landmarks[4]
    fingers_extended = [
        index_tip.y < landmarks[6].y,  
        middle_tip.y < landmarks[10].y,  
        ring_tip.y < landmarks[14].y,   
        pinky_tip.y < landmarks[18].y  
    ]

    index_finger_left = index_tip.x < landmarks[5].x  
    index_finger_right = index_tip.x > landmarks[5].x  

    if all(fingers_extended):
        return "open_tab"
    elif all([not f for f in fingers_extended]):
        return "close_tab"
    elif fingers_extended[0] and fingers_extended[1] and not any(fingers_extended[2:]):
        return "refresh"
    elif index_finger_left and not any(fingers_extended[1:]):
        return "swipe_left"
    elif index_finger_right and not any(fingers_extended[1:]):
        return "swipe_right"
    elif fingers_extended[0] and fingers_extended[1] and fingers_extended[2] and not fingers_extended[3] and wrist.y > middle_tip.y:
        return "scroll_up"
    elif not fingers_extended[0] and not fingers_extended[1] and not fingers_extended[2] and fingers_extended[3] and thumb_tip.y < wrist.y:
        return "scroll_down"
    elif fingers_extended[0] and not fingers_extended[1] and not fingers_extended[2] and fingers_extended[3]:
        return "play_pause"
    return None


def perform_action(gesture):
    if gesture == "swipe_left":
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    elif gesture == "swipe_right":
        pyautogui.hotkey('ctrl', 'tab')
    elif gesture == "scroll_up":
        pyautogui.press('pageup')
    elif gesture == "scroll_down":
        pyautogui.press('pagedown') 
    elif gesture == "open_tab":
        pyautogui.hotkey('command', 't')
    elif gesture == "close_tab":
        pyautogui.hotkey('command', 'w')
    elif gesture == "refresh":
        pyautogui.hotkey('command', 'r')
    elif gesture == "play_pause":
        pyautogui.press("space")

def handle_gesture_control(frame, results):
    global last_action_time
    current_time = time.time()
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            gesture = get_finger_status(landmarks)
            
            if gesture and (current_time - last_action_time) > cooldown_time:
                perform_action(gesture)
                last_action_time = current_time
                return gesture_actions.get(gesture, "Unknown Gesture") 
    
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    return None  