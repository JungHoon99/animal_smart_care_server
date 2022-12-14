import asyncio
import websockets
from ast import literal_eval
import MySqlConnect
from Phone import PhoneDataServer
from device import DeviceDataServer

async def dataServer(websocket, path):
    data = await websocket.recv()
    data = literal_eval(data)
    print(data)
    await websocket.send("Hello")
    if(data['code'] == 'device'):
        your_Code = {"Connect": "Success"}
        await websocket.send("device")
        await DeviceDataServer.Main(websocket,path)
        
        
    elif(data['code'] == 'phone'):
        print("Phone : Connect")
        your_Code = {"Connect": "Success"}
        await websocket.send("phone")
        await PhoneDataServer.Main(websocket,path)
        