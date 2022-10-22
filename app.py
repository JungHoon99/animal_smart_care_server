import asyncio
import websockets
from ast import literal_eval

Room = {}

async def device(websocket,data):
    Room[data['roomNumber']]

async def User(websocket):
    pass
async def Main(websocket, path):
    ClientList.add(websocket)
    data = await websocket.recv()
    data = literal_eval(data)
    if(data['tick'])
    
    
    
    

start_server = websockets.serve(Main, "0.0.0.0", 5050)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
