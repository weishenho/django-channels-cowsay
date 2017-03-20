# In consumers.py
from channels import Group
from channels.sessions import channel_session
import time


#Group("chat").send({"text": "time",})
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message):
    Group("chat").send({
        "text": "hvh",
    })

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)