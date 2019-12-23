import asyncio
import websockets

async def test(websocket, path):
    data = await websocket.recv()
    await websocket.send("success")

start_server = websockets.serve(test, "localhost", 443)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

