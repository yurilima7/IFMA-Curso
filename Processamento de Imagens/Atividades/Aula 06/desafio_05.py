import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")
rot = 0
blue = (255, 0, 0)
points = [0, 0]

rows, cols = img.shape[:2]

def capPoints(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.clear()
        points.insert(0, x), points.insert(1, y)

cv2.namedWindow('Resultado Rot')
cv2.setMouseCallback('Resultado Rot', capPoints)

while 1:
    key = cv2.waitKey(1)

    Matriz = cv2.getRotationMatrix2D((points[0], points[1]), rot, 1)
    res = cv2.warpAffine(img, Matriz, (cols, rows))
    cv2.circle(res, (points[0], points[1]), 5, blue, -1)
    cv2.imshow('Resultado Afim Rot', res)

    if key & 0xFF == ord('r'):
        rot = 0 if rot > 360 else rot + 10

    elif key & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()