---
title: learn grpc
date: 2016-09-10 17:57:59
tags: grpc
---

## install basic tools

1. update pip
```
python -m pip install --upgrade pip
```


2. install grpc
```
python -m pip install grpcio
```

3. install grpc-tools

```
python -m pip install grpcio-tools
```

## learn gprc by example

1. download grpc and change directory to example
```
# Clone the repository to get the example code:
git clone https://github.com/grpc/grpc
# Navigate to the "hello, world" Python example:
cd grpc/examples/python/helloworld
```

2. run server
```
python greeter_server.py
```

3. run client
```
python greeter_client.py
```

## update a grpc service

1. change directory to .proto
```
vi ../../proto/HelloWorld.proto

```
2. Generate gRPC code
```
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
```

* **helloworld_pb2.py** which contains our generated request
and response classes
* **helloworld_pb2_grpc.py** which contains our
generated client and server classes

3. update server
```
class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

  def SayHelloAgain(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)
...
```

4. update client
```

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
```

5. run server & client
