import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")

rows, cols = img.shape[:2]

Matriz = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)

res = cv2.warpAffine(img, Matriz, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Resultado Afim Rot', res)

cv2.waitKey(0)
cv2.destroyAllWindows()