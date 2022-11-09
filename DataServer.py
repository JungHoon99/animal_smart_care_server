import asyncio
import websockets
from ast import literal_eval
import MySqlConnect

async def dataServer(websocket, path):
    data = await websocket.recv()
    print(data)
    await websocket.send("Hello Dark!")
    data = await websocket.recv()
    print(data)
    await websocket.send("Hello Dark!websocket")
    data = await websocket.recv()
    print(data)
    await websocket.send("Hello Darkss!")