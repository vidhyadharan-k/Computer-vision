import cv2

img = cv2.imread('Resources/images/fourpics.png')


imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgray,(7,7),1)
imgcontour = img.copy()
imgcanny = cv2.Canny(img,50,50)

def getContours(img):
    contours,Hierarchy = cv2.findContours(imgcanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgcontour,cnt,-1,(0,0,255),2)
        peri = cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.05*peri,True)
        print(len(approx))
        objectcor = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        if objectcor == 3:
            objectype = "triangle"
        elif objectcor == 4:
            asprat = w/float(h)

            if asprat>0.95 and asprat<1.05:
                objectype = 'square'
            else:
                objectype="rectangle"
        elif objectcor>4:
                objectype == 'circle'

        cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.putText(imgcontour,objectype,(x+(w//2)-10,(y+(h//2))+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

cv2.imshow("original",img)
cv2.imshow("canny",imgcanny)

getContours(imgcanny)
cv2.imshow("contour",imgcontour)
cv2.waitKey(0)
