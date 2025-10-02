from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2 per minute", "1 per second"],
    storage_uri="redis://localhost:6379",
    strategy="fixed-window"
)


@app.route('/hello/<name>')
@limiter.limit("1 per 10 seconds", key_func=lambda: f"{get_remote_address()}-{request.view_args.get('name')}")
# @limiter.limit("10 per minute")
def hello_world(name: str):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(port=5100, host="0.0.0.0")
