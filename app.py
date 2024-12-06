from flask import Flask, render_template, request
    from flask_socketio import SocketIO, emit
    import random

    app = Flask(__name__)
    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('message')
    def handle_message(data):
        print('received message: ' + data)
        emit('response', {'data': 'Hello!'})

    if __name__ == '__main__':
        socketio.run(app, debug=True)
