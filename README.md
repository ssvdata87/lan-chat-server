💬 LAN Chat App

A simple real-time chat application built with FastAPI, WebSockets, HTML, CSS, and JavaScript.
This app lets multiple users chat with each other while connected to the same Wi-Fi / LAN network, without needing the internet.

🚀 Features

📡 Real-time messaging using WebSockets

🌐 Works across multiple devices on the same LAN

⚡ Fast and lightweight (FastAPI + Uvicorn backend)

🎨 Simple and responsive chat UI (HTML, CSS, JS)

📝 Previous messages are sent to new users on join

🛠️ Tech Stack

Backend: FastAPI, WebSockets, Uvicorn

Frontend: HTML, CSS, JavaScript

Dependencies: Listed in requirements.txt

📂 Project Structure
lan-chat-server/
│── templates/
│   └── index.html     # Chat UI
│── server.py          # FastAPI + WebSocket server
│── requirements.txt   # Python dependencies
│── .gitignore         # Ignored files (venv, __pycache__, etc.)
│── README.md          # Documentation
│── LICENSE            # Open-source license

▶️ Installation & Usage
1️⃣ Clone the repository
git clone https://github.com/ssvdata87/lan-chat-server
cd lan-chat-server

2️⃣ Create a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the server
python server.py

5️⃣ Open in browser

On your computer:
👉 http://localhost:8765

On another device connected to the same Wi-Fi:
👉 http://<your-local-IP>:8765

(Find your local IP using ipconfig on Windows or ifconfig on Linux/Mac.)

💡 Future Enhancements

👤 Add user nicknames / login system

💾 Store chat history in a database

📎 File sharing support

🌙 Dark mode theme

📜 License

This project is licensed under the Apache 2.0 License – free to use, modify, and share.  
                              Apache License
                           Version 2.0, January 2004

⚡ Made with ❤️ using FastAPI + WebSockets
