import cv2
import numpy as np

img = cv2.imread("Processamento de Imagens/images/ifma-caxias.jpg")
imgIF = cv2.imread("Processamento de Imagens/images/logo-if.jpg")

imgIF = cv2.resize(imgIF, (200, 100), interpolation = cv2.INTER_AREA)

# logo no topo
rows, cols, channels = imgIF.shape

# trecho da imagem
roi = img[0 : rows, 0 : cols]

# criando máscara
imgIFgray = cv2.cvtColor(imgIF, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(imgIFgray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

# remove máscara onde for preciso
img_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# filtra somente a máscara obtida pelo threshold
imgIF_fg = cv2.bitwise_and(imgIF, imgIF, mask = mask)

i = cv2.add(img_bg, imgIF_fg)

img[0: rows, 0: cols] = i

cv2.imshow('Resultado', img)

cv2.waitKey(0)
cv2.destroyAllWindows()