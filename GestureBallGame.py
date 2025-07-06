import cv2
import mediapipe as mp
import numpy as np
import time
import math
import random

# Initialize the video capture object to get frames from the default webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Track a maximum of 1 hand
mp_draw = mp.solutions.drawing_utils  # For drawing hand landmarks

# Game configuration
screen_width = 1000
screen_height = 700
ball_radius = 30
ball_color = (0, 255, 0)  # Green color for the ball
ball_pos = [random.randint(ball_radius, screen_width - ball_radius),
            random.randint(ball_radius, screen_height - ball_radius)]  # Random ball position

# Initialize the game state
tap_count = 0  # Number of taps
start_time = time.time()  # Record the start time of the game
game_duration = 30  # Game lasts for 30 seconds
tapped = False  # Flag to ensure the ball is only tapped once per position

while True:
    # Capture a frame from the webcam
    success, frame = cap.read()
    if not success :
        break

    # Flip the frame horizontally (like looking in a mirror)
    frame = cv2.flip(frame, 1)

    # Resize the frame to the defined screen dimensions
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Convert the frame to RGB for MediaPipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to get hand landmarks
    result = hands.process(frame_rgb)

    # Track the elapsed time and remaining time
    current_time = time.time()
    elapsed_time = int(current_time - start_time)
    remaining_time = game_duration - elapsed_time

    # Check if the game time is over
    if remaining_time <= 0:
        cv2.putText(frame, f"Time's Up! Taps: {tap_count}", (80, 240), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        cv2.imshow("Hand Ball Game", frame)
        
        # Wait for 3 seconds or until 'q' is pressed to quit
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            break
        else:
            # Reset the game
            tap_count = 0
            start_time = time.time()
            ball_pos = [random.randint(ball_radius, screen_width - ball_radius),
                        random.randint(ball_radius, screen_height - ball_radius)]
        continue

    # If hands are detected in the frame
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the x and y coordinates of the index finger tip (landmark 8)
            cx = int(hand_landmarks.landmark[8].x * screen_width)
            cy = int(hand_landmarks.landmark[8].y * screen_height)

            # Draw a circle on the index finger position
            cv2.circle(frame_rgb, (cx, cy), 5, (0, 0, 0), cv2.FILLED)

            # Calculate the distance between the index finger and the ball's position
            distance = math.hypot(cx - ball_pos[0], cy - ball_pos[1])

            # Check if the finger is close enough to the ball (within ball radius) and hasn't tapped yet
            if distance < ball_radius and not tapped:
                tap_count += 1  # Increment tap count
                tapped = True  # Set tapped flag to True
                # Randomize the ball's position after a tap
                ball_pos = [random.randint(ball_radius, screen_width - ball_radius),
                            random.randint(ball_radius, screen_height - ball_radius)]
            elif distance > ball_radius:
                tapped = False  # Reset the tapped flag if the finger is not close enough to the ball

            # Draw the hand landmarks and connections
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Draw the ball on the frame
    cv2.circle(frame, (ball_pos[0], ball_pos[1]), ball_radius, ball_color, -1)

    # Display the remaining time and tap count on the screen
    cv2.putText(frame, f"Time: {remaining_time}s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f"Taps: {tap_count}", (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Show the frame with the ball and hand landmarks
    cv2.imshow("Hand Ball Game", frame)

    # Break the loop if the 'q' key is pressedx 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
