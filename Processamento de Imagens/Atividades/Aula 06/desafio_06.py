import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")
rot = 0
cosRad, sinRad = np.cos(np.deg2rad(rot)), np.sin(np.deg2rad(rot))
matrizRot = np.array([[cosRad, sinRad],
                      [-sinRad, cosRad]])

cv2.imshow('Original', img)

def direta():
    rows, cols = img.shape[:2]
    imgDireta = np.zeros(img.shape, np.uint8)

    for i in range(0, rows):
        for j in range(0, cols):
            (x, y) = (np.matmul([j, i], matrizRot)).astype(int)

            if x >= 0 and x < cols and y >= 0 and y < rows:
                imgDireta[y, x] = img[i, j]

    return imgDireta

def indireta():
    rows, cols = img.shape[:2]
    imgIndireta = np.zeros(img.shape, np.uint8)
    matrizRotInv = np.linalg.inv(matrizRot)

    for i in range(0, rows):
        for j in range(0, cols):
            (x, y) = (np.matmul([j, i], matrizRotInv)).astype(int)

            if x >= 0 and x < cols and y >= 0 and y < rows:
                imgIndireta[i, j] = img[y, x]

    return imgIndireta

d = direta()
i = indireta()

cv2.imshow('Direta', d)
cv2.imshow('Indireta', i)

while 1:
    key = cv2.waitKey(1)

    if key & 0xFF == ord('r'):
        rot = 0 if rot > 360 else rot + 10

        cosRad, sinRad = np.cos(np.deg2rad(rot)), np.sin(np.deg2rad(rot))
        matrizRot = np.array([[cosRad, sinRad],
                            [-sinRad, cosRad]])

        d = direta()
        i = indireta()

        cv2.imshow('Direta', d)
        cv2.imshow('Indireta', i)

    elif key & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()