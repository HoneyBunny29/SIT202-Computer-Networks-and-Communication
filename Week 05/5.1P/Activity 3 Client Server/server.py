from socket import *
serverPort = 11500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is listening")

while True:
    message, clientaddress = serverSocket.recvfrom(2048)
    message = message.decode()
    ClientSendMessage1 = str(message) + " is received"

    num_characters = len(message)
    print(f"Received message: '{ClientSendMessage1}' with {num_characters} characters")

    serverSocket.sendto(ClientSendMessage1.encode(), clientaddress)