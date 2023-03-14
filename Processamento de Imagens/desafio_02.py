import cv2
from random import randint
import numpy as np

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c = randint(0, len(COLORS)-1)
        cv2.circle(frame, (x, y), 10, COLORS[c], -1)
        cv2.imshow('Video', frame)

video = cv2.VideoCapture("Processamento de Imagens/videos/IFMA Campus Caxias.mp4")

frame_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)

cv2.namedWindow('Video')

if not video.isOpened():
    print('Erro ao acessar!')
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    newVideo = cv2.VideoWriter("Processamento de Imagens/videos/new_video.avi", fourcc, 
                               int(fps), (int(frame_width), int(frame_height)), False)
    
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            cv2.setMouseCallback('Video', draw)

            newVideo.write(frame)
       
            cv2.imshow('Video', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        else: break

video.release()
newVideo.release()
cv2.destroyAllWindows()