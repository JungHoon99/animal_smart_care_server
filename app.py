import asyncio
import websockets
from ast import literal_eval
import threading

Room = {}

# kind가 0일때 실행되는 함수 -> 
async def device(websocket,data):
    Room[data['roomNumber']]={'device':websocket,'client':[]}
    TList =[]
    try:
        # send_Img를 스레드로 동작
        send_t = threading.Thread(target='send_Img', args=(websocket,data['roomNumber']))
        send_t.start()
        TList.append(send_t)
    except:
        del Room[data['roomNumber']]
        
    for i in TList:
        i.join()

#device에서 전송되는 이미지를 받아서 접속한 Client에게 전송
def send_Img(websocket,RoomNb):
    while(1):
        data = websocket.recv()
        tmp = Room[RoomNb]['client'].copy()
        print('send')
        for i in tmp:
            try:
                i.send()
            except:
                print("Client Error")
                Room[RoomNb]['client'].remove(i)

                
# kind가 1일때 실행되는 함수 -> 안드로이드에서 접속시 실행
async def User(websocket,data):
    TList =[]
    if(data['roomNumber'] not in Room):
        await websocket.send("Not Connet Room")
        return 'Falsse'
    else:
        await websocket.send("Connect Room")
    
    Room[data['roomNumber']]['client'].append(websocket)
    send_t = threading.Thread(target='User_command', args=(websocket,data['roomNumber']))
    send_t.start()
    TList.append(send_t)
    
    for i in TList:
        i.join()

#recv command to user send
def User_command(websocket, roomNumber):
    while(1):
        data = websocket.recv()
        try:
        	Room[roomNumber]['device'].send(data)
        except:
            print("Device Error")
        
        
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

start_server = websockets.serve(Main, "0.0.0.0", 5050)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()