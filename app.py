import asyncio
import websockets

async def call(websocket):
    pass

async def accept(websocket, path): 
    while True:
        data = await websocket.recv()
        print("receive : " + data)
        await websocket.send("echo : " + data)

start_server = websockets.serve(accept, "0.0.0.0", 5050)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
