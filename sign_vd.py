'bkklz'
import cv2
import pickle
import numpy as np

cap=cv2.VideoCapture("video.mp4")

def check(frame1):

    spacecounter=0
    for pos in list:
        x,y=pos

        crop=frame1[y:y+15, x:x+26]
        count=cv2.countNonZero(crop)
        #print("count", count)

        if count<150:
            color=(0,255,0)
            spacecounter+=1
        else:
            color=(0,0,255)

        cv2.rectangle(frame,pos,(pos[0]+26, pos[1]+15),color,2)

    #cv2.putText(frame,f"bos: {spacecounter}/{len(list)}", (15,24),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),4)
    cv2.putText(frame,f"bos: {spacecounter}/{len(list)}", (15,24),cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),3)


with open("parkinglotvd", "rb") as f:
    list=pickle.load(f)

while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),1)
    thres=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    median=cv2.medianBlur(thres,5)
    dilates=cv2.dilate(median,np.ones((3,3)),iterations=1)

    check(dilates)


    cv2.imshow("park",frame)
    #cv2.imshow("gray", gray)
    #cv2.imshow("median", median)

    if cv2.waitKey(200) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    
