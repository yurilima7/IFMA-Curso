import cv2

img = cv2.imread("Processamento de Imagens/images/opencv_low.png")

w, h = (int(10 * img.shape[0]), int(10 * img.shape[1]))
res1 = cv2.resize(img, (h, w), interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img, (h, w), interpolation = cv2.INTER_NEAREST) # metodo de interpolação mais próxima

cv2.imshow('res1', res1)
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()