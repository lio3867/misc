#!/usr/bin/env python
# encoding: utf-8

"""

Simple interface

pip install flask-socketio
pip install eventlet
pip install eventlet==0.26 (for Windows)

python -m simple_visu.run

"""
from __future__ import print_function, division, absolute_import

from colorama import Fore, Style            # Color in the Terminal
import os
import yaml
import json
op = os.path
opd, opb, opj = op.dirname, op.basename, op.join

import threading
import webbrowser
from sys import platform as _platform
##
from flask import Flask, render_template, request, redirect     # Flask imports
from flask_socketio import SocketIO, emit
from simple_visu.modules.pages.define_all_pages import *
from simple_visu.modules.util_interf import *

platf = find_platform()

if platf == 'win':
    import gevent as server
    from gevent import monkey
    monkey.patch_all()
else:
    import eventlet as server
    server.monkey_patch()

Debug = True                                             # Debug Flask

app = Flask(__name__)
# upload directory from the Dropzone
app.config['UPLOADED_PATH'] = opj(os.getcwd(), 'simple_visu', 'upload')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'F34TF$($e34D'
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    '''
    Websocket connection
    '''
    # with open('mini_server/nb_pics.yaml', 'r') as f_r:
    #     nb_pics = yaml.load(f_r, Loader=yaml.FullLoader)
    #     print(f'nb_pics is { nb_pics }')
    # emit('nb_pics', nb_pics)
    emit('response', 'Connected', broadcast=True)
    server.sleep(0.05)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    '''
    '''
    platf = find_platform()
    print(f'platf is { platf }')
    dmp = define_main_page(platf)
    return render_template('index_folder.html', **dmp.__dict__)


def send_nb_pics():
    '''
    Sending the number of pictures
    '''
    with open('mini_server/nb_pics.yaml', 'r') as f_r:
        nb_pics = yaml.load(f_r, Loader=yaml.FullLoader)
        print(f'nb_pics is { nb_pics }')
    emit('nb_pics', nb_pics)


@app.route('/shutdown')
def shutdown():
    '''
    Shutting down the server.
    '''
    shutdown_server()

    return 'Server shutting down...'


def message_at_beginning(host, port):
    '''
    '''
    print(Fore.YELLOW + f"""
    ***************************************************************
    Launching the simple_visu server program !!!

    address: { host }:{ port }

    Addons :

    pip install flask-socketio
    pip install gevent (Windows)
    pip install eventlet

    Change each time the port !!!
    perhaps using random port..

    """)


if __name__ == '__main__':

    init(app.config)                # clean last processings and upload folders

    port = 5999
    host = '0.0.0.0'                                # simple_visu.run
    print("host is ", host)
    message_at_beginning(host, port)
    print(Style.RESET_ALL)
    socketio.run(app, port=port, host=host)
