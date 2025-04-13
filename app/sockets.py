from . import socketio
#app/sockets.py

def socket_events(socketio):
      @socketio.on('connect')
      def handle_connect():
          print("Client connected")

      @socketio.on('disconnect')
      def handle_disconnect():
          print("Client disconnected")
