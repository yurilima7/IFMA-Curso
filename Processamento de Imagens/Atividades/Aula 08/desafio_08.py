import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/noise.jpg")

media = cv2.medianBlur(img, 9)

cv2.imshow("ORIGINAL", img)
cv2.imshow("MEDIAN BLUR", media)

cv2.waitKey(0)
cv2.destroyAllWindows()