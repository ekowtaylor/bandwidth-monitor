import datetime
import logging
import os

from flask import Flask, render_template

from data.data_analyzer import get_data, get_summary
from main import WEB_PORT

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'bandwidth-monitor-master')
template_dir = os.path.join(template_dir, 'web')
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

started = None


@app.route('/settings')
def settings():
    template = render_template('settings.html')

    return template

@app.route('/')
def index():
    global started

    current_values = get_data(f'select time_timestamp, download_rate from bandwidth_data order by time_timestamp asc')

    data = []
    categories = []

    for value in current_values:
        timestamp = float(value[0])

        categories.append(str(parse_datetime(timestamp)))

        download_rate = value[1]
        data.append(download_rate)

    requests, download_rate_avg, upload_rate_avg = get_summary(time_started=started)

    template = render_template('index.html', categories=categories, data=data, requests=requests,
                               download_rate_avg=download_rate_avg, upload_rate_avg=upload_rate_avg,
                               start_time=parse_datetime(started),
                               this_time=parse_datetime(datetime.datetime.now().timestamp()))
    return template


def parse_datetime(f):
    return datetime.datetime.fromtimestamp(f).strftime("%m/%d/%Y, %H:%M:%S")


def main(web_port):
    print('[INFO]: Starting web server...')

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.CRITICAL)

    app.env = 'production'
    app.run(debug=False, port=web_port)
