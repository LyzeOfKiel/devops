'''Flask HTTP time server'''

import os
from datetime import datetime
import pytz
from flask import Flask, render_template, request, make_response

MOSCOW_TZ = pytz.timezone('Europe/Moscow')
VISITS_FILE = 'visits/visits.txt'

def create_visits():
    dirname = os.path.dirname(VISITS_FILE)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if not os.path.exists(VISITS_FILE):
        os.mknod(VISITS_FILE)

def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.update(config)

    create_visits()

    @app.route('/')
    def get_moscow_time():
        '''Index page endpoint'''
        moscow_time = datetime.now(MOSCOW_TZ).strftime('%H:%M:%S')
        with open(VISITS_FILE, 'a') as visits_file:
            visits_file.write(f"{request.remote_addr} {moscow_time}\n")
        return render_template('index.html', time=moscow_time)

    @app.route('/visits')
    def visits():
        '''Get all index page visits'''
        with open(VISITS_FILE, 'r') as visits_file:
            response = make_response(visits_file.read(), 200)
            response.mimetype = "text/plain"
        return response

    return app
