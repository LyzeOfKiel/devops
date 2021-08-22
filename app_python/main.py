'''Flask HTTP time server'''

from datetime import datetime
import pytz
from flask import Flask, render_template

MOSCOW_TZ = pytz.timezone('Europe/Moscow')

app = Flask(__name__)

@app.route("/")
def get_moscow_time():
    '''Index page endpoint'''
    moscow_time = datetime.now(MOSCOW_TZ).strftime('%H:%M:%S')
    return render_template('index.html', time=moscow_time)
