import cv2
face_detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("IMG-20191005-WA0177.jpg",1)
faces=face_detect.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
for (x,y,h,w) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,455,0),3)
cv2.imshow("Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


