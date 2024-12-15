from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import socket
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class CGMinerAPI:
    def __init__(self, host="127.0.0.1", port=4028):
        self.host = host
        self.port = port

    def send_command(self, command, parameter=None):
        """
        Send a command to the CGMiner API using a socket.
        """
        payload = {"command": command}
        if parameter:
            payload["parameter"] = parameter

        try:
            with socket.create_connection((self.host, self.port), timeout=10) as sock:
                request = json.dumps(payload) + "\n"
                sock.sendall(request.encode("utf-8"))
                response = b""
                while True:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk

                response_str = response.decode("utf-8").strip()
                response_str = response_str.rstrip("\u0000")  # Remove trailing null character

                return json.loads(response_str)
        except Exception as e:
            return {"error": f"Socket error: {str(e)}"}

    def summary(self):
        return self.send_command("summary")

    def pools(self):
        return self.send_command("pools")

    def restart(self):
        return self.send_command("restart")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the homepage with a form to send commands.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/command", response_class=HTMLResponse)
async def send_command(
    request: Request, command: str = Form(...), parameter: str = Form(None)
):
    """
    Handle user commands and parse the response for the UI.
    """
    api = CGMinerAPI()
    if command == "summary":
        result = api.summary()
    elif command == "pools":
        result = api.pools()
    elif command == "restart":
        result = api.restart()
    else:
        result = {"error": "Unknown command"}

    return templates.TemplateResponse("result.html", {"request": request, "data": result})
