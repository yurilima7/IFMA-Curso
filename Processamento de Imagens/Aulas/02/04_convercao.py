# convertendo no momento de acesso
import cv2

img = cv2.imread('Processamento de Imagens/images/logo-if.jpg', cv2.IMREAD_COLOR)
imgGray = cv2.imread('Processamento de Imagens/images/logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# shape retorna o formato das imagens
print('shape original {}'.format(img.shape))
print('shape gray {}'.format(imgGray.shape))

# size retorna o tamanho das imagens
print('size original {}'.format(img.shape))
print('size gray {}'.format(imgGray.shape))

# dtype retorna os formatos dos pixels
print('dtype original {}'.format(img.dtype))
print('dtype gray {}'.format(imgGray.dtype))

cv2.imshow('Original', img)
cv2.imshow('Gray', imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
