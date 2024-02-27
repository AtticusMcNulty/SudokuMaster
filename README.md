# Microservice Communication Contract
## Introduction
This document outlines the communication contract for interacting with the microservice implemented using ZeroMQ (ZMQ).

## How to Programmatically REQUEST Data
To programmatically request data from the microservice, follow these steps:
  1. Establish Connection: First, establish a connection to the microservice by creating a ZeroMQ socket of type REQ and connecting it to the microservice's address.
  2. Send Request: Send a request message to the microservice using the send_string() method of the socket object. The request message should be a string containing the input data according to the specified format.

### Example call from microservice/test files:
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request_data = "123_a"
socket.send_string(request_data)
```

## How to Programmatically RECEIVE Data
The microservice will respond to requests based on the input provided. To programmatically receive data from the microservice, follow these steps:
  1. Receive response: The microservice will receive the request sent by the client.
  2. Process response: Process the received request according to the specified requirements.
  3. Send Response: Send a response message back to the client using the send_string() method of the ZeroMQ socket (optional).

### Example receive from microservice/test files:
```
response = socket.recv_string()
## process response
## if needed, send response
```

## UML Diagram - Created using PlantUML

![Uploading plantuml.svg…]()
