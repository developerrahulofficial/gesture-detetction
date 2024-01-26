import cv2
import mediapipe as mp
import pyautogui

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# For drawing on frames
mp_drawing = mp.solutions.drawing_utils

# Get screen resolution
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

prev_x = None
prev_y = None

while cap.isOpened():
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Check if hand landmarks are available
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            pinky_mcp = landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

            # Detect swipe gestures using index finger tip coordinates
            x, y = int(index_tip.x * screen_width), int(index_tip.y * screen_height)

            if prev_x is not None and prev_y is not None:
                dx = x - prev_x
                dy = y - prev_y

                if abs(dx) > abs(dy):  # Horizontal swipe
                    if dx > 50:  # Threshold for swipe right
                        pyautogui.press('right')
                    elif dx < -50:  # Threshold for swipe left
                        pyautogui.press('left')
                else:  # Vertical swipe
                    if dy > 50:  # Threshold for swipe down
                        pyautogui.press('down')
                    elif dy < -50:  # Threshold for swipe up
                        pyautogui.press('up')

            prev_x = x
            prev_y = y

            # Detect rock gesture (thumb tip close to pinky MCP)
            distance_thumb_pinky = ((thumb_tip.x - pinky_mcp.x) ** 2 + (thumb_tip.y - pinky_mcp.y) ** 2) ** 0.5

            if distance_thumb_pinky < 0.1:  # Threshold for rock gesture
                pyautogui.press('space')

    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
