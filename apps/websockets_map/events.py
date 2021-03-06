from django_socketio import events

@events.on_connect()
def connect(request, socket, context):
    message = {"action" : "system-info", "text" : "connexion ok"}
    socket.send(message)

@events.on_subscribe(channel="^room-")
def connect(request, socket, context, channel):
    message = {"action" : "system-info", "text" : " - on subscribe ok"}
    socket.send(message)

@events.on_message(channel="^room-")
def message(request, socket, context, message):
    if message["action"] == "moveend":
        socket.send_and_broadcast_channel(message)



