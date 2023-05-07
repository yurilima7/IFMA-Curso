import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Processamento de Imagens/images/atividade_aula11.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (200, 200), interpolation = cv2.INTER_CUBIC)

kernel = np.ones((9, 9), dtype = np.uint8)
kernelDilation = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

# erosão da primeira modificação
erosion = cv2.erode(img, kernel, iterations = 3)
# dilatação necessária para a terceira imagem
dilation = cv2.dilate(img, kernel, iterations = 5)
# erosão aplicada a imagem dilatada anteriormente com o kernel de elipse
erosion_kd = cv2.erode(dilation, kernelDilation, iterations = 5)
# dilatação eliptica aplicada a erosão feita na linha anterior
dilation_rounded = cv2.dilate(erosion_kd, kernelDilation, iterations = 3)

plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(222), plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB)), plt.title("Erosion")
plt.subplot(223), plt.imshow(cv2.cvtColor(dilation_rounded, cv2.COLOR_BGR2RGB)), plt.title("Dilation")

plt.tight_layout()
plt.show()