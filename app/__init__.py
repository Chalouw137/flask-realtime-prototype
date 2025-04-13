from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

eventlet.monkey_patch()

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/')
    def index():
        return render_template('index.html')

    # Attach SocketIO to the app
    socketio.init_app(app)

    # Define socket events directly here or import them
    @socketio.on('message')
    def handle_message(data):
        print('Received message:', data)
        socketio.send(data)

    return app
