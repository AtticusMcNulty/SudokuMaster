import zmq

def validate_input(input_string):
    # Validate the input based on your requirements
    if len(input_string) != 5:
        return False
    code, char = input_string.split("_")
    if not (code.isdigit() and len(code) == 3 and char in ['a', 'b', 'c']):
        return False
    return True

def microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Listening on port 5555

    while True:
        # Wait for next request from client
        request = socket.recv_string()
        print(f"Received request: {request}")

        # Validate the request
        if validate_input(request):
            # Process the request
            code, char = request.split("_")
            if code not in codes_seen:
                codes_seen.add(code)
                response = "valid"
            else:
                response = "invalid"
        else:
            response = "invalid"

        # Send reply back to client
        socket.send_string(response)

    socket.close()
    context.term()

if __name__ == "__main__":
    codes_seen = set()  # To store codes already seen
    microservice()
