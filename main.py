import cv2
import mediapipe as mp 
import numpy as np 
mp_drawing = mp.solutions.drawing_utils #This gives all drawing utilities like for visualising poses and stuff
mp_pose = mp.solutions.pose #grabbing pose estimation models

# Video Feed!
cap = cv2.VideoCapture(0) #Setting our video cap device to device '0'
##Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read() #storing webcam feed in frame

        # Detect and render stuff
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # RECOLOR OPENCV IMAGE TO MEDIAPIPE FORMAT
        image.setflags(write=0) # optimization for performance and shi

        # Make detection
        results = pose.process(image) # storing images in results

        # Make the image writable again for further processing
        image.setflags(write=1)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # RECOLORING MEDIAPIPE IMAGE TO OPENCV FORMAT

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y].value
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y].value
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y].value
            
            # Function to Calculate angles
            def calculate_angle(a,b,c):
                a = np.array(a) #Start
                b = np.array(b) #Mid
                c = np.array(c) #End

                radians = np.arctan2(c[1]-b[1], c[0]-b[0])-np.arctan2(a[1]-b[1], a[0]-b[0]) # Calculating radians
                angle = np.abs(radians*180.0/np.pi) # Calculating the angle itself

                if angle > 180.0: # Making the angle based on 180 degrees instead of 360
                    angle = 360-angle
                return angle

            # Using the function to calculate angles
            angle = calculate_angle(shoulder,elbow,wrist)

            #Visualize angle
            cv2.putText(image, str(angle),
                        tuple(np.multiply(elbow, [1280, 720]).astype(int)),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AAA)

            # # Visualize angle
            # cv2.putText(image, str(angle),
            #              tuple(np.multiply(elbow, [frame.shape[1], frame.shape[0]]).astype(int)),
            #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            
                
            print(landmarks)
        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS) # Using our drawing utilities to get result model coords

        cv2.imshow('Mediapipe Feed', image) #popup window

        if cv2.waitKey(10) & 0xFF == ord('q'): #if window is closed or q is pressed:
            break

    cap.release() #bye webcam
    cv2.destroyAllWindows() #ded window


#49:38