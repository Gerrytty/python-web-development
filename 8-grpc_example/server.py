# server.py
import grpc
from concurrent import futures

import hello_pb2
import hello_pb2_grpc

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    # 1. Unary RPC
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}!")

    # 2. Server streaming
    def StreamHello(self, request, context):
        for i in range(3):
            yield hello_pb2.HelloReply(message=f"{i+1}: Hello, {request.name}")

    # 3. Client streaming
    def SendNames(self, request_iterator, context):
        names = [req.name for req in request_iterator]
        joined = ", ".join(names)
        return hello_pb2.HelloReply(message=f"Received names: {joined}")

    # 4. Bidirectional streaming
    def Chat(self, request_iterator, context):
        for req in request_iterator:
            yield hello_pb2.HelloReply(message=f"Echo: {req.name}")


if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    port = 5051
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()

