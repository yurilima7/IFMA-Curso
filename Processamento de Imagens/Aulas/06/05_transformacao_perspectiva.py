import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")

pts1 = [[200, 100], [400, 100], [50, 400], [550, 400]]
pts2 = [[0, 0], [300, 0], [0, 300], [300, 300]]

Matriz = cv2.getPerspectiveTransform(np.float32(pts1), np.float32(pts2))

res = cv2.warpPerspective(img, Matriz, (300, 300))

for pt in pts1:
    cv2.circle(img, pt, 5, (0, 0, 255), -1)

for pt in pts2:
    cv2.circle(res, pt, 5, (0, 0, 255), -1)

cv2.imshow('Original', img)
cv2.imshow('Resultado Perspectiva Transform', res)

cv2.waitKey(0)
cv2.destroyAllWindows()