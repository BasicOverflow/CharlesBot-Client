import pyaudio
import pickle
import websockets
 
FORMAT = pyaudio.paInt16
CHANNELS = 1 #2
RATE = 16000 #44100
CHUNK = 4096 
WAVE_OUTPUT_FILENAME = "C:/Users/peter/Desktop/poo2.wav"
audio = pyaudio.PyAudio()


async def ws_audio_client(url):
    '''Used to send peripheral data straight to webAPI'''
    stream = audio.open(format=FORMAT, channels=CHANNELS,
            rate=RATE, input=True,
            frames_per_buffer=CHUNK)
    # try:
    async with websockets.connect(url) as ws:
        print("Starting Audio Recording...")
        # start Recording
        while True:
            data = stream.read(CHUNK)
            await ws.send(pickle.dumps(data))
            
            resp = await ws.recv()
            if resp == "": continue
            print(resp) 

    # except Exception as e:
    #     # stop Recording
    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()
    #     print(f"({url}) - Audio client error: {e}")


                

if __name__ == "__main__":
    import asyncio
    # asyncio.get_event_loop().run_until_complete(ws_audio_client("ws://localhost:12345"))
    # asyncio.get_event_loop().run_until_complete(ws_audio_client("ws://10.0.0.253:8004/ws/audio/Laptop"))
    asyncio.get_event_loop().run_until_complete(ws_audio_client("ws://10.0.0.253:8005"))

