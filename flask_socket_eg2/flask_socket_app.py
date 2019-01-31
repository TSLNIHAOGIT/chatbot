from flask import Flask, render_template
from flask_socketio import SocketIO
import random
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('my event')
def my_event(message):
    print(message['data'])


if __name__ == '__main__':
    socketio.run(app)