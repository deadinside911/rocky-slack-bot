import os
import requests

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv

from landsat import make_landsat_image


load_dotenv()


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/rocky-hello")
def rocky_hello(ack, respond, command):
    ack()

    respond(f"hello!", response_type="in_channel")


@app.command("/landsat")
def make_landsat_name(ack, respond, command, client):
    ack()
    
    name = str(command['text']).upper()
    make_landsat_image(name)
    filepath = f"{command['text']}.png"
    
    response = client.files_getUploadURLExternal(
        filename=os.path.basename(filepath),
        length=os.path.getsize(filepath),
    )
    upload_url = response["upload_url"]
    file_id = response["file_id"]
    
    with open(filepath, "rb") as file:
        requests.post(upload_url, data=file.read())
    
    client.files_completeUploadExternal(
        files=[{"id": file_id, "title": name}],
        channel_id=command["channel_id"],
    )

    os.remove(filepath)
    
    respond(f"hello, just finishing up making {command['text']} in landsat", response_type="in_channel")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()