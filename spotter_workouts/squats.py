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
exercise_name = "Squats"  

with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        def calculate_angle(a,b,c):
            a = np.array(a)
            b = np.array(b)
            c = np.array(c)
    
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
                
            if angle >180.0:
                angle = 360-angle
                
            return angle

        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            # Calculate angle
            angle = calculate_angle(hip, knee, ankle)

            # Visualize angle
            cv2.putText(image, str(angle), 
                        tuple(np.multiply(knee, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )

            # Squat counter logic
            if angle > 160:
                stage = "up"
            if angle < 100 and stage == 'up':
                stage = "down"
                counter += 1

        except:
            pass

        # Render counter
        cv2.rectangle(image, (0,0), (225,73), (0,0,0), -1)
        cv2.putText(image, 'REPS', (15,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA
                    )
        cv2.putText(image, 'STAGE', (85,12), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(image, stage, 
                    (80,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA
                    )

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

    cap.release()
    cv2.destroyAllWindows()
