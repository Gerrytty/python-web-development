from flask import Flask
import requests
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import time
import threading
import logging
from sentry_sdk.integrations.logging import LoggingIntegration

logging_integration = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)

dsn = "http://0b8811a1b5724d74a053216096ee2b54@23.140.40.144:8000/1"

sentry_sdk.init(
    # dsn="http://0b8811a1b5724d74a053216096ee2b54@glitchtip.example.com/1",
    dsn=dsn,
    integrations=[FlaskIntegration(), logging_integration]
)

HEARTBEAT_URL = "http://23.140.40.144:8000/api/0/organizations/student/heartbeat_check/a52ff105-daaf-4401-a312-e31ed52c7051/"
HEARTBEAT_INTERVAL = 9

logger = logging.getLogger(__name__)

def send_heartbeat():
    while True:
        try:
            response = requests.post(HEARTBEAT_URL, timeout=5)
            print("response finished with code", response.status_code)
        except Exception as e:
            print("Exception occurred", e)
        time.sleep(HEARTBEAT_INTERVAL)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def err():
    division_by_zero = 1 / 0


@app.route('/debug')
def trigger_error():
    err()


@app.route('/exception')
def exception():
    raise Exception("some exception")


@app.route("/error_log")
def error_log():
    logger.error("some logged error")
    return "ok"


heartbeat_thread = threading.Thread(target=send_heartbeat, daemon=True)
heartbeat_thread.start()


if __name__ == '__main__':
    app.run()
