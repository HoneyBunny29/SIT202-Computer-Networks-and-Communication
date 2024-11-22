from socket import *

serverName = "127.0.0.1"
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = "Hello"
clientSocket.sendto(message.encode(), (serverName, serverPort))

serverReply, serverAddress = clientSocket.recvfrom(2048)
print(f"Received from server: {serverReply.decode()}")

name = input("Enter your name: ")
clientSocket.sendto(name.encode(), (serverName, serverPort))

serverReply, serverAddress = clientSocket.recvfrom(2048)
print(f"Received from server: {serverReply.decode()}")

clientSocket.close()
