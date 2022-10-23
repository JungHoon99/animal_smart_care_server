import asyncio
import websockets
from ast import literal_eval
import threading

Room = {}

async def device(websocket,data):
    Room[data['roomNumber']]={'device':websocket,'client':[]}
    try:
        # send_Img를 스레드로 동작
        send_t = threading.Thread(target='send_Img', args=(websocket,data['roomNumber']))
        send_t.start()
    except:
        del Room[data['roomNumber']]

#device에서 전송되는 이미지를 받아서 접속한 Client에게 전송
def send_Img(websocket,RoomNb):
    while(1):
        data = websocket.recv()
        tmp = Room[RoomNb]['client'].copy()
        for i in tmp:
            try:
                i.send()
            except:
                Room[RoomNb]['client'].remove(i)

async def User(websocket,data):
    if(data['roomNumber'] not in Room):
        await websocket.send("Not Connet")
        return
    
    Room[data['roomNumber']]['client'].append(websocket)
    print(Room)
    
async def Main(websocket, path):
    data = await websocket.recv()
    data = literal_eval(data)
    if(data['kind'] == 0):
        await device(websocket,data)
    else:
        await User(websocket,data)

start_server = websockets.serve(Main, "0.0.0.0", 5050)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
