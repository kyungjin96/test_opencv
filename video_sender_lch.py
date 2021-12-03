import cv2 as cv
cap = cv.VideoCapture(0)

import socket
sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 480 * 640 * 3 / 20 = 46080
perlength = int( (480 * 640 * 3) / 20)
reallength = perlength + 1

while cap.isOpened():
    ret, frame = cap.read()
    mat = cv.resize(frame, (480,640))
    num = frame.flatten()
    str = num.tostring()
    
    for i in range(3):
        sender.sendto(bytes([i]) + str[i*perlength:(i+1)*perlength],('192.168.16.27',7778))
        pass
    pass