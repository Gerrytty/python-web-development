from flask import Flask
import time
from flask_caching import Cache
from flask import request

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)


@app.route('/hello/<name>')
def hello_world(name: str):
    name = long_function(name)
    return f'Hello {name}'


@cache.cached(timeout=50, key_prefix='long_function')
def long_function(name: str):
    time.sleep(5)
    return f"{name} !!!"


if __name__ == '__main__':
    app.run(port=5100, host="0.0.0.0")
