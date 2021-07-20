#install cv2 or python-opencv using pip

import cv2

#use lbpcascade or haarcascade xml files as training data for the program.

faceCascade = cv2.CascadeClassifier("Resources\lbpcascade_frontalface_improved.xml")

#use cv2.VideoCapture(0) if youre using a default webcam ; and (1) for a usb connected secondary webcam

cap = cv2.VideoCapture(1)
while True:
    success,img=cap.read()

   
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgray,1.1,4)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Face", (x + (w // 2) - 10, (y + (h // 2)) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
  
    # cv2.imshow("window_name" ,image_file) will display the captured feed in a window with the specified name. 
    cv2.imshow("face",img) 
    
    #Press q to stop the video and chage the paramenter in ord() to assign your own quitting key.



    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
