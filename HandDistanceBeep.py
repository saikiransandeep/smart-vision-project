import cv2
import mediapipe as mp
import numpy as np
import winsound  # For Windows beep sound

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Constants for distance calculation
KNOWN_WIDTH = 8.0  # cm
FOCAL_LENGTH = 500  # Adjust if needed

# Function to calculate distance
def calculate_distance(perceived_width):
    if perceived_width == 0:
        return 0
    return (KNOWN_WIDTH * FOCAL_LENGTH) / perceived_width

# Start webcam
cap = cv2.VideoCapture(0)

# Set a threshold (e.g. 20 cm to trigger beep)
BEEP_DISTANCE_THRESHOLD = 20.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x_min, y_min = float('inf'), float('inf')
            x_max, y_max = 0, 0

            for lm in hand_landmarks.landmark:
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                x_min, y_min = min(x_min, x), min(y_min, y)
                x_max, y_max = max(x_max, x), max(y_max, y)

            perceived_width = x_max - x_min
            distance = calculate_distance(perceived_width)

            if distance < BEEP_DISTANCE_THRESHOLD and distance > 0:
                # Frequency (Hz), Duration (ms)
                winsound.Beep(1000, 150)  # Beep when hand is close

            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, f'Distance: {distance:.2f} cm', (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Distance Measurement', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
