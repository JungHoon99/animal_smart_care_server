from MySqlConnect import MufiData
import asyncio
import websockets
from ast import literal_eval
import json

async def Main(websocket,path):
    data = await websocket.recv()
    data = literal_eval(data)
    md  = MufiData()
    sendMessage = {"Title":"","message":""}
    
    if(data["kind"]=="select"):
        data = md.selectdb(data["message"])
        sendMessage["Title"] = "Select success"
        sendMessage["message"] = data
        sendStr = json.dumps(sendMessage)
        await websocket.send(sendStr)
    elif(data["kind"]=="insert"):
        data = md.insertdb(data["message"])
        sendMessage["message"] = data
        sendStr = json.dumps(sendMessage)
        await websocket.send(sendStr)
    else:
        sendMessage["Title"] = "Try Again"
        await websocket.send(str(sendMessage))