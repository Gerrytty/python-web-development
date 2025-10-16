import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask
import requests
import time
import threading

import logging

logging.getLogger()

logging.error("some text")

dsn = "http://4cbe37f5c9e149e8b65d7a8085839044@23.140.40.144:8000/3"
monitor_url = "http://23.140.40.144:8000/api/0/organizations/student/heartbeat_check/9d9a2f75-31b4-4241-b072-fe250f59790d/"

sentry_sdk.init(
    dsn=dsn,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/error')
def trigger_error():
    # division_by_zero = 1 / 0

    raise Exception("any exception")


def monitor():
    while True:

        resp = requests.post(monitor_url)
        print(resp.status_code)

        time.sleep(9)


heartbeat_thread = threading.Thread(target=monitor, daemon=True)
heartbeat_thread.start()

app.run()