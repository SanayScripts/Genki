import cv2
import mediapipe as mp
import numpy as np
import csv
import datetime
import os
from tkinter import messagebox

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

counter = 0
stage = None

start_time = datetime.datetime.now()

csv_file_path = "res/session_data.csv"

# Ensure the directory exists
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

# Define the exercise name
exercise_name = "OH Press"  

with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
   
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        def calculate_angle(a, b, c):
            a = np.array(a)
            b = np.array(b)
            c = np.array(c)

            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        try:
            landmarks = results.pose_landmarks.landmark

            l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            angle_l = calculate_angle(l_shoulder, l_elbow, l_wrist)
            angle_r = calculate_angle(r_shoulder, r_elbow, r_wrist)

            cv2.putText(image, str(angle_l),
                        tuple(np.multiply(l_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, str(angle_r),
                        tuple(np.multiply(r_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            if angle_l < 45 and angle_r < 45:
                stage = "down"
            if (angle_l > 160 and angle_r > 160) and stage == "down":
                stage = "up"
                counter += 1

        except:
            pass

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.rectangle(image, (0, 0), (360, 73), (0, 0, 0), -1)

        cv2.putText(image, 'REPS', (15, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), (15, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.putText(image, 'STAGE', (100, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, stage if stage else "-", (100, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

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
