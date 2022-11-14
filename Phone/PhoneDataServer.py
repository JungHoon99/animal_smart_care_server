from MySqlConnect import MufiData
import asyncio
import websockets
from ast import literal_eval

async def Main(websocket,path):
    data = await websocket.recv()
    data = literal_eval(data)
    md  = MufiData()
    sendMessage = {"Title":"","message":""}
    if(data["kind"]=="select"):
        data = md.selectdb(data["message"])
        sendMessage["Title"] = "Select success"
        sendMessage["message"] = data
        await websocket.send(str(sendMessage))
    elif(data["kind"]=="insert"):
        pass
    else:
        sendMessage["Title"] = "Try Again"
        await websocket.send(str(sendMessage))