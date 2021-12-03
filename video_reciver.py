import socket
import numpy as np
import cv2

recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


perlength = int( (480 * 640 * 3) / 20)
reallength = perlength + 1

recevier.bind(('192.168.16.101',7778))
array = []
while True:
    try:

        message, address = recevier.recvfrom(reallength)
        # byterpair=  recevier.recvfrom(reallength)

        # message = byterpair[0]
        # address = byterpair[1]


        # print(message,' ' ,address)

        str = message[1:]
        array[message[0]] = str
        

        num_array = b''
        if message[0] == 19:
            for i in range(20):
                num_array +=array[i]
            frame = np.fromstring(num_array, dtype= np.uint8)
            frame = frame.reshape(480,640,3)
            cv2.imshow('video', frame)


        pass

             

    except KeyboardInterrupt:
        break

