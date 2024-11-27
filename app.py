from web_socket_server import WebSocketServer, socketio, app
from flask import render_template

app = WebSocketServer().create_app()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message_package):
    print(f'Received message: {message_package}')
    socketio.emit('message', message_package)

@app.route('/')
def index():
    return render_template('JoinChat.html')

@app.route('/ChatRoom')
def indexChat():
    return render_template('ChatRoom.html')
    

if __name__ == '__main__':
    socketio.run(app)