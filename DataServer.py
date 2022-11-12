import asyncio
import websockets
from ast import literal_eval
import MySqlConnect
from Phone import PhoneDataServer
from Devices import DeviceDataServer

async def dataServer(websocket, path):
    data = await websocket.recv()
    literal_eval(data)
    
    if(data['code'] == 'device'):
        your_Code = {"Connect": "Success"}
        await websocket.send("device")
        await DeviceDataServer.Main(websocket,path)
        
        
    elif(data['code'] == 'Phone'):
        your_Code = {"Connect": "Success"}
        await websocket.send("phone")
        await PhoneDataServer.Main(websocket,path)
        