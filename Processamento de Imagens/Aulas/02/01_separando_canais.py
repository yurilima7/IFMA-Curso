import cv2

img = cv2.imread('Processamento de Imagens/images/logo-if.jpg')

b, g, r = cv2.split(img) # separando os 3 canais

cv2.imshow('BGR', img)
cv2.imshow('RED', r)
cv2.imshow('GREEN', g)
cv2.imshow('BLUE', b)

cv2.waitKey(0)
cv2.destroyAllWindows()