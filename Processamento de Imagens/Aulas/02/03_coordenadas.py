import cv2

img = cv2.imread('Processamento de Imagens/images/logo-if.jpg')

print(img[0,0])
print(img[0,8])

roi = img[0:150, 0:150]
cv2.imshow('IMAGE', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()