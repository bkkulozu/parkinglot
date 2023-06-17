'bkklz'
import cv2
import pickle

try:
    with open("parkinglots", "rb") as f:
        #list.pickle.load(f)
        list=pickle.load(f)

except:
    list=[]

def mouse(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        list.append((x,y))

    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(list):
            x1,y1=pos
            if x1<x<x1+26 and y1<y<y1+15:
                list.pop(i)

    with open("parkinglots", "wb") as f:
        pickle.dump(list,f)

while True:
    img=cv2.imread("first_frame.png")
    print(list)
    for r in list:
        cv2.rectangle(img,r,(r[0]+26, r[1]+15),(255,0,0),2)

    cv2.imshow("img",img)
    cv2.setMouseCallback("img", mouse)

    if cv2.waitKey(1) &0xFF==ord("q"):
        break

cv2.destroyAllWindows()

