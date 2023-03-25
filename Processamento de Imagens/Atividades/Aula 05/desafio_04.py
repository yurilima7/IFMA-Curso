import cv2
import numpy as np

PATH = 'Processamento de Imagens\images\logo-if.jpg'

image = cv2.imread(PATH)

brilho = 0
contraste = 1

def contBrilho(img, b):

    res = np.zeros(img.shape, np.uint8)

    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            p1 = img[y, x]
            res[y, x] = np.maximum(np.minimum(p1 + (b, b, b), (255, 255, 255)), (0, 0, 0))

    return res

def contrasteImg(img, b):

    res = np.zeros(img.shape, np.uint8)

    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            p1 = img[y, x]
            res[y, x] = np.maximum(np.minimum(p1 * b, (255, 255, 255)), (0, 0, 0))

    return res

def negativoImg(img):

    res = np.zeros(img.shape, np.uint8)

    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            p1 = img[y, x]
            res[y, x] = np.maximum((255, 255, 255) - p1, (0, 0, 0))

    return res

cv2.namedWindow('ajustes')
rest = image
cv2.imshow('ajustes', rest)

while(1):
    key = cv2.waitKey(20)

    if key & 0xFF == ord('a'):
        brilho = min(brilho + 25, 255)
        rest = contBrilho(image, brilho)
        cv2.imshow('ajustes', rest)

    elif key & 0xFF == ord('z'):
        brilho = max(brilho - 25, 0)
        rest = contBrilho(image, brilho)
        cv2.imshow('ajustes', rest)

    elif key & 0xFF == ord('s'):
        contraste = min(contraste + 0.25, 2.0)
        rest = contrasteImg(image, contraste)
        cv2.imshow('ajustes', rest)

    elif key & 0xFF == ord('x'):
        contraste = max(contraste - 0.25, 0.5)
        rest = contrasteImg(image, contraste)
        cv2.imshow('ajustes', rest)

    elif key & 0xFF == ord('n'):
        rest = negativoImg(rest)
        cv2.imshow('ajustes', rest)

    elif key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# const - pimg
# 255 - 155 = 100
# 255 - 100 = 155
# 255 - 255 = 0
# 255 - 0 = 255
# 255 - (-200) = 255
# 255 - 255 = 0