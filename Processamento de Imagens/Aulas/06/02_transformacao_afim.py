import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")

rows, cols = img.shape[:2]

Matriz = np.float32([[1, 0, 100], [0, 1, 50]]) # transf em x(horizontal) e y(vertical)
res = cv2.warpAffine(img, Matriz, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Resultado Afim', res)

cv2.waitKey(0)
cv2.destroyAllWindows()