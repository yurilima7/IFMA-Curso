import cv2
import numpy as np

img = cv2.imread('Processamento de Imagens/images/wallpaper01.png')

height = img.shape[0] // 3
width = img.shape[1] // 3

print(height, width)

def reduce(image):
    out = np.zeros((height, width, 3), np.uint8)
    
    for i in range (1, height * 3, 3):
        for j in range (1, width * 3, 3):
            out[(i - 1) // 3][(j - 1) // 3] = image[i][j]

    return out

def reduce_mean(image):
    out = np.zeros((height, width, 3), np.uint8)
    
    for i in range (1, height * 3, 3):
        for j in range (1, width * 3, 3):
            out[(i - 1) // 3][(j - 1) // 3] = np.uint8(image[i - 1 : i + 2, j - 1: j + 2]).sum() // 9

    return out

img_mod = reduce(img)
img_mean = reduce_mean(img)

cv2.imshow('Imagem', img_mod)
cv2.imshow('Imagem Mean', img_mean)

cv2.waitKey(0)
cv2.destroyAllWindows()