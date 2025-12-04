# client.py
import grpc
import hello_pb2
import hello_pb2_grpc

port = 5051

if __name__ == "__main__":

    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = hello_pb2_grpc.GreeterStub(channel)

    # 1. Unary RPC
    response = stub.SayHello(hello_pb2.HelloRequest(name="Julia"))
    print("Unary:", response.message)

    # 2. Server streaming
    print("Server streaming:")
    for response in stub.StreamHello(hello_pb2.HelloRequest(name="Mert")):
        print(" ", response.message)

    # 3. Client streaming
    print("Client streaming:")
    names = ["Alina", "Ben", "Islam"]
    responses = (hello_pb2.HelloRequest(name=n) for n in names)
    resp = stub.SendNames(responses)
    print(" ", resp.message)

    # 4. Bidirectional streaming
    print("Bidirectional chat:")

    def requests():
        for n in ["One", "Two", "Three"]:
            yield hello_pb2.HelloRequest(name=n)


    for r in stub.Chat(requests()):
        print(" ", r.message)
