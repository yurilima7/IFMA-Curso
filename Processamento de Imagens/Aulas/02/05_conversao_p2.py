import cv2

img = cv2.imread('Processamento de Imagens/images/logo-if.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

cv2.imshow('HSV', hsv)
cv2.imshow('RGB', rgb)
cv2.imshow('GRAY', gray)
cv2.imshow('BGRA', bgra)

print(bgra.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()