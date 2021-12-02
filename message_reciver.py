import socket

reciver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
reciver.bind('192.168.16.27',7778)

while True:
    bytepair = reciver.recvfrom(1024)

    message = bytepair[0]
    address = bytepair[1]

    print(message, ', ', address)