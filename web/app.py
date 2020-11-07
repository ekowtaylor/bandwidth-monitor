import datetime
import logging
import os

from flask import Flask, render_template

from data.data_analyzer import get_data

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'bandwidth-monitor-master')
template_dir = os.path.join(template_dir, 'web')
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

started = None


@app.route('/')
def index():
    global started

    current_labels = get_data(f'select time_timestamp from bandwidth_data '
                              f'order by time_timestamp asc')

    labels = []
    for label in current_labels:
        t = label
        f = float(t[0])
        labels.append(datetime.datetime.fromtimestamp(f))

    current_values = get_data(f'select time_timestamp, download_rate from bandwidth_data order by time_timestamp asc')

    data = []
    categories = []

    for value in current_values:
        f = float(value[0])
        strftime = datetime.datetime.fromtimestamp(f).strftime("%m/%d/%Y, %H:%M:%S")

        categories.append(str(strftime))

        data.append(value[1])

    template = render_template('index.html', categories=categories, data=data)
    return template


def main():
    print('[INFO]: Starting web server...')

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    app.run(debug=False, port=8600)
