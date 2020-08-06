#!/usr/bin/env python
from flask import Flask, render_template, session, request, flash
from flask_socketio import SocketIO, emit 
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

my_value = 5278

@app.route('/')
def index():
    return render_template('slider_bar.html')

@socketio.on('client_event')
def client_msg(msg):
    print(slidervalue)

@socketio.on('connect_event')
def connected_msg(msg):
    print(msg)





if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port='5001')