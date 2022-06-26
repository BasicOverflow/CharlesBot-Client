import cv2


BORDER_COLOR = (255,255,255)

face_cascade1 = cv2.CascadeClassifier("traindata/haarcascade_frontalcatface.xml")
# face_cascade2 = cv2.CascadeClassifier("traindata/haarcascade_frontalcatface_extended.xml")
body_cascade = cv2.CascadeClassifier("traindata/haarcascade_fullbody.xml")
profile_face_cascade = cv2.CascadeClassifier("traindata/haarcascade_profileface.xml")
upperbody_cascade = cv2.CascadeClassifier("traindata/haarcascade_upperbody.xml")
lowerbody_cascade = cv2.CascadeClassifier("traindata/haarcascade_lowerbody.xml")


def draw_rectangle(detect_object,frame):
	if len(detect_object) == 0:
		return
	else:
		for (x,y,w,h) in detect_object:
			#Draw rectangle around detected objects in the iterable
			cv2.rectangle(frame,(x,y),(x+w,y+h),BORDER_COLOR,2)


def haar_cascade(frame):
		#if not already given as grayscale, 
		try:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #the way image data is normalized for object detection
		except:
			gray = frame
		#Detect different objects through the harr cascade
		faces1 = face_cascade1.detectMultiScale(gray,1.3,5)
		# faces2 = face_cascade2.detectMultiScale(gray,1.3,5)
		bodies = body_cascade.detectMultiScale(gray,1.3,5)
		prof_faces = profile_face_cascade.detectMultiScale(gray,1.3,5)
		upper_bodies = upperbody_cascade.detectMultiScale(gray,1.3,5)
		lower_bodies = lowerbody_cascade.detectMultiScale(gray,1.3,5)
		#apply function to draw rectangles on the objects within the original frame
		draw_rectangle(faces1,frame)
		# draw_rectangle(faces2,frame)
		draw_rectangle(bodies,frame)
		draw_rectangle(upper_bodies,frame)
		draw_rectangle(lower_bodies,frame)
		#return original frame with rectangles drawn on it
		return frame
	
	

