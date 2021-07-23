HandTracking Module:
Uses Opencv and Mediapipe hand tracking system to track and identify key points on the hands.
Coded as a module to be used for further projects.
OOP approach to hand detection using class handDetection.
...

FingerCounting:
Imports and uses HandTracking module to create an object "detector" of the class handDetector.
Uses id and their corresponding position of the points (available in mediapipe website) to check if the finger is closed or not.
<img src="https://google.github.io/mediapipe/images/mobile/hand_landmarks.png">
Open fingers are counted and added to display the no of fingers shown.
Works for a single hand , but be extended upto multiple hands by altering the parameter handNo in the function findPosition()-> HandTrackingModule.
