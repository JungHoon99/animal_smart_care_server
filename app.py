import asyncio
import websockets
from ast import literal_eval
import DataServer

Room = {}

# kind가 0일때 실행되는 함수 -> 라즈베리파이 접속시 실행
async def device(websocket,data):
    Room[data['roomNumber']]={'device':websocket,'client':[]}
    print(Room)
    try:
        send_t = asyncio.create_task(send_Img(websocket,data['roomNumber']))
    except:
        del Room[data['roomNumber']]
        return
        
    await send_t
    del Room[data['roomNumber']]

# device에서 전송되는 이미지를 받아서 접속한 Client에게 전송
async def send_Img(websocket,RoomNb):
    while(1):
        data = await websocket.recv()
        tmp = Room[RoomNb]['client'].copy()
        for i in tmp:
            try:
            	await i.send(data)
            except:
                Room[RoomNb]['client'].remove(i)
                print('LOST Client')

# kind가 1일때 실행되는 함수 -> 안드로이드에서 접속시 실행
async def User(websocket,data):
    TList =[]
    if(data['roomNumber'] not in Room):
        await websocket.send("Not Connet Room")
        return 'Falsse'
    else:
        await websocket.send("Connect Room")
    send_t = asyncio.create_task(User_command(websocket,data['roomNumber']))
    
    Room[data['roomNumber']]['client'].append(websocket)
    print(Room)
    await send_t
    Room[data['roomNumber']]['client'].remove(websocket)
    
# recv command to user send
async def User_command(websocket, roomNumber):
    while(1):
        data = await websocket.recv()
        try:
        	await Room[roomNumber]['device'].send(data)
        except:
            print("Device Error")
            break
        
        
# Websocket Server로 들어오면 가장 먼저 실행되는 함수
# 처음 받는 데이터는 json형태로 입력을 받는다.
# 데이터 안에 있는 요소들은{ 'kind' : ( <int> 0 or 1 ) , 'roomNumber' : ( <str> 기기 일련번호 ) }
async def Main(websocket, path):
    data = await websocket.recv()
    print("Connect")
    data = literal_eval(data)
    if(data['kind'] == 0):
        await device(websocket,data)
    else:
        await User(websocket,data)


start_server = websockets.serve(Main, "0.0.0.0", 5050, ping_interval=None)
start_data_server = websockets.serve(DataServer.dataServer, "0.0.0.0", 5051, ping_interval=None)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_data_server)
asyncio.get_event_loop().run_forever()