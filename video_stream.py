import cv2
import asyncio
import websockets
import pickle
#from picamera.array import PiRGBArray
#from picamera import PiCamera



# def piCam_streamer(res=(640,480)): #For the Pi
#     camera = PiCamera()
#     camera.resolution = res
#     #Define actual capture object
#     rawCap = PiRGBArray(camera,size=res)
#     #Allow camera to warm up
#     time.sleep(0.1)
#     #Loop through frames
#     for frame in camera.capture_continuous(rawCap,format="bgr",use_video_port=True):
#         #3D array, containing width.height, and num of channels. Ready for cv
#         frame = frame.array
#         #Perform actions and transformations on the frame, return
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         #apply object detection to frame
#         #gray = haar_cascade(gray)
#         #convert to bytes before returning grayscaled frame
#         _,encoded = cv2.imencode(".jpg",gray)
#          #this is necessary for frame capture to work properly
#         if cv2.waitKey(1) == 27:
#             break
#         #Truncate
#         rawCap.truncate(0)
#         yield bytes(encoded) #encode grayscaled image before returning
#         #print(getsizeof(encoded))
#         #cv2.imshow("PiNode1",gray)


async def vid_streamer(cap):
    # global cap
    # cap = cv2.VideoCapture(0)
    while True:
        # await asyncio.sleep(0.0000000001)
        ret ,frame = cap.read()
        if not ret:
            continue
        # print(ret)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #convert to bytes before returning grayscaled frame
        _,gray = cv2.imencode(".JPG",gray)
        #this is necessary for frame capture to work properly
        if cv2.waitKey(1) == 27: 
            break
        #encode grayscaled image before returning
        yield gray
        # print(getsizeof(encoded))
        # cv2.imshow("PiNode1 VidStream",gray)
        cv2.destroyAllWindows()

    cap.release()
    cv2.destroyAllWindows()
        
    
async def ws_video_client(url):
    '''Used to send peripheral data straight to webAPI'''
    #TODO: add exception handling
    cap = cv2.VideoCapture(0)
    async with websockets.connect(url) as ws:
        print("Started Video Recording...")
        while True:
            async for frame in vid_streamer(cap):
                # print(type(frame))
                await ws.send(pickle.dumps(frame))
        cap.release()
        cv2.destroyAllWindows()




    

if __name__ == "__main__":
    asyncio.run(ws_video_client("ws://10.0.0.129:8004/ws/video/Laptop"))
