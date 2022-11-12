import MySqlConnect
import asyncio
import websockets

async def Main(websocket,path):
    data = websocket.recv()
    literal_eval(data)
    md  = MySqlConnect()
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