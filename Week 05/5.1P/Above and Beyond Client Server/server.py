from socket import *
serverPort = 11500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is listening")

while True:

    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()
    print(f"Received message: '{message}'")

    response = "Hello, What’s your name?"
    serverSocket.sendto(response.encode(), clientAddress)

    name, clientAddress = serverSocket.recvfrom(2048)
    name = name.decode()
    print(f"Received name: '{name}'")

    finalResponse = f"Hello {name}, Welcome to SIT202"
    serverSocket.sendto(finalResponse.encode(), clientAddress)