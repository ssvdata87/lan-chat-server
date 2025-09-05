from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []       # Connected clients
messages = []      # Message log

@app.get("/")
async def get_chat():
    return FileResponse("templates/index.html")

@app.get("/all_messages")
async def all_messages():
    return {"messages": messages}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print(f"✅ Client connected: {websocket.client.host}")

    # Send previous messages to newly connected client
    for msg in messages:
        await websocket.send_text(msg)

    try:
        while True:
            data = await websocket.receive_text()
            messages.append(data)
            print(f"📩 Received: {data}")
            # Broadcast to all clients
            for client in clients:
                await client.send_text(data)
    except WebSocketDisconnect:
        print(f"❌ Client disconnected: {websocket.client.host}")
        clients.remove(websocket)

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8765, reload=True)
