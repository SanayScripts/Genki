import cv2
import mediapipe as mp
import numpy as np
import csv
import datetime
import os
import tkinter as tk
from tkinter import messagebox

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return int(angle)  # Round down to nearest integer

# Function to show message box for saving session data
def show_save_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = messagebox.askyesno("Genki", "Do you want to save the session data?")
    return result

# Initialize variables
counter = 0
stage = None

# Initialize webcam
cap = cv2.VideoCapture(0)




csv_file_path = "res/session_data.csv"

# Ensure the directory exists
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

# Define the exercise name
exercise_name = "Leg Raises"

# Initialize pose detection
with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
    start_time = datetime.datetime.now()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Unable to capture frame.")
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Perform pose detection
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Calculate angles and count reps
        try:
            if results.pose_landmarks is not None:
                landmarks = results.pose_landmarks.landmark

                # Calculate angles between chest, hips, and ankles
                l_chest = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                           landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                l_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                           landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                r_chest = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                r_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                angle_l = calculate_angle(l_chest, l_hip, l_ankle)
                angle_r = calculate_angle(r_chest, r_hip, r_ankle)

                cv2.putText(image, str(angle_l),
                tuple(np.multiply(r_hip, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                # Count reps
                if angle_l > 160 and angle_r > 160:
                    stage = "down"
                if (angle_l < 110 and angle_r < 110) and stage == "down":
                    stage = "up"
                    counter += 1

        except Exception as e:
            print("Error:", e)

        # Visualize angle information and rep counter
        cv2.rectangle(image, (0, 0), (360, 73), (0, 0, 0), -1)
        cv2.putText(image, 'REPS', (15, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), (15, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, 'STAGE', (100, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, stage if stage else "-", (100, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        # Render pose landmarks
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Genki', image)

        if cv2.waitKey(10) & 0xFF == ord('q'): 
            confirmation = messagebox.askquestion("Genki", "Are you sure you want to save the data to CSV?")
            if confirmation == 'yes':
                end_time = datetime.datetime.now()
                session_duration = end_time - start_time
                formatted_duration = str(session_duration)[:-7]
                
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([exercise_name, str(formatted_duration), start_time.strftime("%d/%m/%Y"), str(counter)])

                messagebox.showinfo("Genki", "Data saved to CSV successfully.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
