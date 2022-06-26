import cv2


def cascade(detect_object,img):
    if len(detect_object) == 0:
        return 
    else:
        for (x,y,w,h) in detect_object:
            #Draw rectangle around it
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 2)



face_cascade1 = cv2.CascadeClassifier("traindata/haarcascade_frontalcatface.xml")
face_cascade2 = cv2.CascadeClassifier("traindata/haarcascade_frontalface_alt.xml")
body_cascade = cv2.CascadeClassifier("traindata/haarcascade_fullbody.xml")
profile_face_cascade = cv2.CascadeClassifier("traindata/haarcascade_profileface.xml")
upper_body_cascade = cv2.CascadeClassifier("traindata/haarcascade_upperbody.xml")
lower_body_cascade = cv2.CascadeClassifier("traindata/haarcascade_lowerbody.xml")


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray",gray)
    faces1 = face_cascade1.detectMultiScale(gray,1.3,5)
    faces2 = face_cascade2.detectMultiScale(gray,1.3,5)
    bodies = body_cascade.detectMultiScale(gray,1.3,5)
    prof_faces = profile_face_cascade.detectMultiScale(gray,1.3,5)
    upper_bodies = upper_body_cascade.detectMultiScale(gray,1.3,5)
    lower_bodies = lower_body_cascade.detectMultiScale(gray,1.3,5)
    #apply rectanglge
    cascade(faces1,img)
    cascade(faces2,img)
    cascade(bodies,img)
    cascade(prof_faces,img)
    cascade(upper_bodies,img)
    cascade(lower_bodies,img)

    #show it
    cv2.imshow("frame",img)
    #Wait for user input to quit 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


def haarcascade(frame):
    #if not already grayscale, convert to grayscale:
    try: 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    except:
        gray = frame
    #Use haar cascade to detect different objects that we have trained for
    faces1 = face_cascade1.detectMultiScale(gray,1.3,5)
    faces2 = face_cascade2.detectMultiScale(gray,1.3,5)
    bodies = body_cascade.detectMultiScale(gray,1.3,5)
    prof_faces = profile_face_cascade.detectMultiScale(gray,1.3,5)
    upper_bodies = upper_body_cascade.detectMultiScale(gray,1.3,5)
    lower_bodies = lower_body_cascade.detectMultiScale(gray,1.3,5)
    #apply rectanglge
    cascade(faces1,frame)
    cascade(faces2,frame)
    cascade(bodies,frame)
    cascade(prof_faces,frame)
    cascade(upper_bodies,frame)
    cascade(lower_bodies,frame)
    #return original frame with the rectangles drawn on it
    return frame



cascade()





