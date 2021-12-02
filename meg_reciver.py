import socket

recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

recevier.bind(('192.168.16.101',7778))
while True:
    try:
        byterpair=  recevier.recvfrom(1024)

        message = byterpair[0]
        address = byterpair[1]


        print(message,' ' ,address)
    except KeyboardInterrupt:
        break