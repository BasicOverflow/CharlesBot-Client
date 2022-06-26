# import cv2
import asyncio
import threading
from video_stream import ws_video_client
from audio_stream import ws_audio_client


url = "ws://10.0.0.129:8004/ws/video/Laptop"

async def peristence_wrapper(func):
    '''Allows client to re-attempt connection to server if initial connection is lost'''
    while True:
        try:
            await func()
        except Exception as e:
            print(f"ERROR: {e}")
            await asyncio.sleep(1)




if __name__ == "__main__": 
    #Init audio & video streaming w/ peristence in seperate threads
    threading.Thread(target=lambda: asyncio.run(peristence_wrapper(lambda: ws_video_client(url)))).start()
    threading.Thread(target=lambda: asyncio.run(peristence_wrapper(lambda: ws_audio_client(url)))).start()





