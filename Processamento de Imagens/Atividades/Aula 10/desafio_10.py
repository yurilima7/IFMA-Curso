import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("Processamento de Imagens/images/new-if.jpg")
imgIF = cv2.imread("Processamento de Imagens/images/new-if_mask.jpg", 0)

cv2.imshow('Inicial', img)

# tamanho da imagem
rows, cols = imgIF.shape

# seleciona o trecho no topo onde ficará a imagem
roi = img[0 : rows, 0 : cols]

ns = cv2.inpaint(roi, imgIF, 3, cv2.INPAINT_NS)

img[0: rows, 0: cols] = ns

cv2.imshow('Resultado', img)
cv2.imshow('Resultado da Remoção NS', ns)

cv2.waitKey(0)
cv2.destroyAllWindows()