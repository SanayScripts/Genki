import cv2
import mediapipe as mp 
import numpy as np 
mp_drawing = mp.solutions.drawing_utils #This gives all drawing utilities like for visualising poses and stuff
mp_pose = mp.solutions.pose #grabbing pose estimation models

# Video Feed!
cap = cv2.VideoCapture(0) # Setting our video cap device to device '0'

# Curl Counter variables
counter_l = 0
counter_r = 0
stage_l = None
stage_r = None

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():   
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False # Making image's writable status as false

        # Make detection
        results = pose.process(image) # storing images in results
        image.flags.writeable = True  # Make the image writable again for further processing
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Recolor back to BGR

        # Writing a function to calculate the angle
        def calculate_angle(a,b,c):
            a = np.array(a) # Start
            b = np.array(b) # Mid
            c = np.array(c) # End
    
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi) # Calculating the angle itself
                
            if angle >180.0: # Making the angle based on 180 degrees instead of 360
                angle = 360-angle
                
            return angle

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates for both arms
            l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Calculate angles for both arms
            angle_l = calculate_angle(l_shoulder, l_elbow, l_wrist)
            angle_r = calculate_angle(r_shoulder, r_elbow, r_wrist)

            # Visualize angles
            cv2.putText(image, str(angle_l),
                        tuple(np.multiply(l_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(image, str(angle_r),
                        tuple(np.multiply(r_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)          

            # Curl counter logic for both arms
            if angle_l > 155:
                stage_l = "down"
            if angle_l < 30 and stage_l == "down":
                stage_l = "up"
                counter_l += 1

            if angle_r > 155:
                stage_r = "down"
            if angle_r < 30 and stage_r == "down":
                stage_r = "up"
                counter_r += 1

        except:
            pass

        # Render curl counter
        # Create a black rectangle for the status box
        cv2.rectangle(image, (0, 0), (360, 73), (0, 0, 0), -1)

        # Rep count for left arm
        cv2.putText(image, 'REPS L', (15, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_l), (15, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        # Stage info for left arm
        cv2.putText(image, 'STAGE L', (100, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, stage_l, (100, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        # Rep count for right arm
        cv2.putText(image, 'REPS R', (200, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter_r), (200, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        # Stage info for right arm
        cv2.putText(image, 'STAGE R', (275, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, stage_r, (275, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
  
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Mediapipe Feed', image) #popup window

        if cv2.waitKey(10) & 0xFF == ord('q'): #if window is closed or q is pressed:
            break

    cap.release() #bye webcam
    cv2.destroyAllWindows() #ded window
