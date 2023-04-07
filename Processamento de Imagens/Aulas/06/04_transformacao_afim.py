import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")

rows, cols = img.shape[:2]

pts1 = [[50, 50], [200, 50], [50, 200]]
pts2 = [[10, 100], [200, 50], [100, 250]]

Matriz = cv2.getAffineTransform(np.float32(pts1), np.float32(pts2))

res = cv2.warpAffine(img, Matriz, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Resultado Afim Transform', res)

cv2.waitKey(0)
cv2.destroyAllWindows()