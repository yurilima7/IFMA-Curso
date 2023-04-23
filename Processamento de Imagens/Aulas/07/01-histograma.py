import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('Processamento de Imagens\images\ifma-caxias.jpg')

# Escala de cinza
imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Escala de Cinza', imagem_pb)

hist = cv2.calcHist([imagem_pb], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.destroyAllWindows()
