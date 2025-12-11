from jsonrpcserver import method, serve, Success

@method
def sum(a, b):
    return Success(a + b)

@method
def subtract(a, b):
    return Success(a - b)


if __name__ == "__main__":
    serve("localhost", 5000)



