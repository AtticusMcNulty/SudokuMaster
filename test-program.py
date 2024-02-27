import zmq

def test_microservice():
    # setup and connect
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # test cases
    test_cases = [
        "123_a",
        "456_b",
        "789_c",
        "123_d",
        "999_a",
        "123",
        "123_",
        "12_a",
        "123_aa",
    ]

    # call microservice for each test case
    for test_case in test_cases:
        print(f"Sending request: {test_case}")
        socket.send_string(test_case)
        response = socket.recv_string()
        print(f"Received response: {response}")

    socket.close()
    context.term()

if __name__ == "__main__":
    test_microservice()
