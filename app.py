import asyncio
import websockets
from ast import literal_eval

Room = {}

async def device(websocket,data):
    Room[data['roomNumber']]={'device':websocket,'client':[]}
    print(Room)

async def User(websocket,data):
    Room[data['roomNumber']]['client'].append(websocket)
    print(Room)
    

async def Main(websocket, path):
    ClientList.add(websocket)
    data = await websocket.recv()
    data = literal_eval(data)
    if(data['kind'] == 0):
        await device(websocket,data)
    else:
        await User(websocket,data)

start_server = websockets.serve(Main, "0.0.0.0", 5050)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
