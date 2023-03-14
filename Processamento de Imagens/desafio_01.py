import cv2
img_original = cv2.imread('Processamento de Imagens/images/original.jpeg')
img_original = cv2.resize(img_original, (300, 400))

gray_img = img_original.copy()

img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

(row, col) = img_original.shape[0:2]

for i in range (row):
    for j in range (col):
        if (img_hsv[i, j] [0] < 170) or (img_hsv[i,j] [0] > 200):
            gray_img[i, j] = sum(img_original[i, j]) * 0.33

cv2.imshow('Original',img_original)
cv2.imshow('Gray',gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()