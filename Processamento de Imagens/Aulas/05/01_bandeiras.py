import cv2
import numpy as np

imagem1 = cv2.imread('Processamento de Imagens/images/bandeira_cxs.jpg')
imagem2 = cv2.imread('Processamento de Imagens/images/bandeira_ma.jpg')

alpha = 0.5
while(1):
    result = cv2.add(imagem1, imagem2)
    result2 = cv2.subtract(imagem1, imagem2)

    cv2.imshow('Operacoes - add', result)
    cv2.imshow('Operacoes - subtract', result2)

    k = cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        alpha = min(alpha + 0.1, 1.0)
    elif k == ord('z'):
        alpha = max(alpha - 0.1, 0.0)
        
cv2.destroyAllWindows()