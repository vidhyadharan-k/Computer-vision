import cv2
import time
import os
import HandTrackingModule as htm
wcam, hcam = 640,480
cap = cv2.VideoCapture(1)
cap.set(3, wcam)
cap.set(4, hcam)
folderPath = "Fingerimages"
myList = os.listdir(folderPath)
print(myList)
overLayList=[]
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    print(f'{folderPath}/{imPath}')
    overLayList.append(image)

pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    #print(lmList)

    if len(lmList) !=0:
        fingers = []
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(0)
        else:
                fingers.append(1)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers = sum(fingers)
        #print(totalFingers)
        h, w, c = overLayList[totalFingers-1].shape
        img[0:h, 0:w] = overLayList[totalFingers-1]
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 255), 25)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,f'FPS:{int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("cam", img)
    cv2.waitKey(1)
