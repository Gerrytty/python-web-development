from flask import Flask
from flask import request

app = Flask(__name__)


def print_hello(name):

    if name == "name":
        raise Exception

    print(f"hello {name}!")


@app.before_request
def check_annotations():
    view_func = app.view_functions.get(request.endpoint)
    if view_func and hasattr(view_func, '_hello_func'):

        # get path variables from Flask request.view_args
        args = request.view_args or {}
        name = args.get("name")

        # call the function
        view_func._hello_func(name)


def hello(name):
    def decorator(func):
        func._hello_func = print_hello
        return func
    return decorator


@app.route('/hello/<name>')
@hello("name")
def hello_world(name: str):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(port=5100, host="0.0.0.0")
