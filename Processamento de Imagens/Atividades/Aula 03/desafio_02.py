import cv2
import numpy as np

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)

COLORS=[BLUE,GREEN]

thickness = 10
oldX, oldY = None, None
isDrawing = False
color = BLUE

def draw(event, x, y, flags, param):
    global oldX, oldY, isDrawing

    if event == cv2.EVENT_LBUTTONDOWN:
        oldX, oldY, isDrawing = x, y, True

    elif event == cv2.EVENT_MOUSEMOVE and isDrawing:
        cv2.line(frame, (oldX, oldY), (x, y), color, thickness)
        oldX, oldY = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.line(frame, (oldX, oldY), (x, y), color, thickness)
        isDrawing = False

video = cv2.VideoCapture("Processamento de Imagens/videos/IFMA Campus Caxias.mp4")

frameWidth = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)

cv2.namedWindow('Video')

if not video.isOpened():
    print('Erro ao acessar!')
else:
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    newVideo = cv2.VideoWriter("Processamento de Imagens/videos/new_video.mp4", fourcc, 
                               int(fps), (int(frameWidth), int(frameHeight)))
    
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            cv2.setMouseCallback('Video', draw)

            key = cv2.waitKey(1)

            if key & 0xFF == ord('c'):
                if color == BLUE:
                    color = GREEN
                else:
                    color = BLUE

            elif key & 0xFF == ord(' '):
                frame[:] = 0

            newVideo.write(frame)
       
            cv2.imshow('Video', frame)

            if key & 0xFF == ord('q'):
                break

        else: break

video.release()
newVideo.release()
cv2.destroyAllWindows()