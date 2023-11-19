from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='templates')

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)