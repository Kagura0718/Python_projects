import imp
from tkinter import EXCEPTION
from unittest import result
from urllib import response
import pyaudio
from requests import session
import websockets
import asyncio
import base64
import json
from api_secrets import API_KEY_ASSEMBLYAI
from openai_helper import ask_computer
#set up parameters
FRAME_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNLES = 1
RATE = 16000

p = pyaudio.PyAudio() #microphone recording

stream = p.open(
    format=FORMAT,
    channels = CHANNLES,
    rate = RATE,
    input = True,
    frames_per_buffer= FRAME_PER_BUFFER
)

# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

#send and receive the data
async def send_receive():
    async with websockets.connect(
        URL,
        ping_timeout = 20,
        ping_interval = 5,
        extra_headers={"Authorization": API_KEY_ASSEMBLYAI}
    ) as _ws:
        await asyncio.sleep(0.1)
        session_begins = await _ws.recv()
        print(session_begins)
        
        async def send():
            #running infintly and listen for incoming data
            while True:
                try:
                    #read microphone input
                    data = stream.read(FRAME_PER_BUFFER, exception_on_overflow= False)
                    #sometime when the websocket connection is too slow, there might be an overflow and then have an exception, which we dont want
                    #convert this or encode it in base 64
                    data = base64.b64decode(data).decode("utf-8")#assemblyAI expect
                    #convert it to JSON object
                    json_data = json.dumps({"audio_data": data})
                    await_ws.send(json_data)
                #
                except websockets.expecitions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, "Not a websocket 4008 error"
                await asyncio.sleep(0.01)
                


        async def receive():
            while True:
                try:
                    #have to wait for the transcription result form AssemblyAI
                    result_str = await _ws.recv()
                    result = json.loads(result_str)
                    prompt = result("text")
                    if prompt and result["message_type"] == "FinalTranscript":
                        print("Me:", prompt)
                        response = ask_computer(prompt)
                        print("Bot:", response)

                except websockets.expecitions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, "Not a websocket 4008 error"

        #combine them in a async io 
        send_result, receive_result = await asyncio.gather(send(), receive())

asyncio.run(send_receive())




