import cv2
import numpy as np

video = cv2.VideoCapture("Processamento de Imagens/videos/IFMA Campus Caxias.mp4")

imgIF = cv2.imread("Processamento de Imagens/images/logo-if.jpg")
imgIF = cv2.resize(imgIF, (200, 100), interpolation = cv2.INTER_AREA)

frameWidth = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)

cv2.namedWindow('Video')

if not video.isOpened():
    print('Erro ao acessar!')
else:
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:

            rows, cols, channels = imgIF.shape

            roi = frame[0 : rows, 0 : cols]

            imgIFgray = cv2.cvtColor(imgIF, cv2.COLOR_BGR2GRAY)
            ret, mask_inv = cv2.threshold(imgIFgray, 125, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask_inv)

            img_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

            imgIF_fg = cv2.bitwise_and(imgIF, imgIF, mask = mask)

            i = cv2.add(img_bg, imgIF_fg)

            frame[0: rows, 0: cols] = i

            cv2.imshow('Video', frame)

            key = cv2.waitKey(20)

            if key & 0xFF == ord('q'):
                break

        else: break

cv2.waitKey(0)
cv2.destroyAllWindows()