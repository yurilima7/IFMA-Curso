import cv2

img = cv2.imread('Processamento de Imagens/images/logo-if.jpg')

b, g, r = cv2.split(img) # separando os 3 canais

res = cv2.merge([r, g, b]) # juntando os canais em uma nova imagem

cv2.imshow('BGR', img)
cv2.imshow('RGB', res)

cv2.waitKey(0)
cv2.destroyAllWindows()