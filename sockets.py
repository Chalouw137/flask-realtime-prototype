from . import socketio

@socketio.on("message")
def handle_message(msg):
    print("Received message: " + msg)
    socketio.emit("response", "Echo: " + msg)
