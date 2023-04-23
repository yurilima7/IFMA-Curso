import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('Processamento de Imagens\images\ifma-caxias.jpg')

# Colorido
cv2.imshow('Colorido', imagem)
color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([imagem], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0, 256])
    
plt.show()