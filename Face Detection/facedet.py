import cv2
faceCascade = cv2.CascadeClassifier("Resources\lbpcascade_frontalface_improved.xml")


cap = cv2.VideoCapture(1)
while True:
    success,img=cap.read()

    imgcanny = cv2.Canny(img,50,50)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgray,1.1,4)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Face", (x + (w // 2) - 10, (y + (h // 2)) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
  

    cv2.imshow("face",img)



    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
