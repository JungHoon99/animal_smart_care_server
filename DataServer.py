import asyncio
import websockets
from ast import literal_eval
import MySqlConnect

async def dataServer(websocket, path):
    data = await websocket.recv()
    literal_eval(data)
    if(data['code'] == 'device'):
        your_Code = {"Connect": "Success"}
        await websocket.send("device")
        
    elif(data['code'] == 'Phone'):
        your_Code = {"Connect": "Success"}
        await websocket.send("phone")
        