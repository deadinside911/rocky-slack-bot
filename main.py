import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web import WebClient
from slack_sdk.socket_mode.websocket_client import SocketModeClient

from dotenv import load_dotenv


load_dotenv()

client = SocketModeClient(
    app_token=os.environ.get("SLACK_APP_TOKEN"), 
    web_client=WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))  
)

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/rocky-hello")
def rocky_hello(ack, respond, command):
    ack()

    respond(f"hello!", response_type="in_channel")


@app.command("/landsat")
def make_landsat_name(ack, respond, command):
    ack()
    respond(f"{command["text"]}", response_type="in_channel")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()