import cv2
import numpy as np

COLOR = (255, 0, 0)
# sequência de moedas
COINS = ['50', '5', '1', '10', '25']
img = cv2.imread('Processamento de Imagens/images/coins.jpeg')

img_blur = cv2.medianBlur(img, 5)
img_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# detecção de circulos
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 100, param1 = 150, param2 = 50)

circles=np.uint(circles[0])

for i in range(len(circles)):
    x, y, r = circles[i]

    cv2.circle(img, (x, y), r, COLOR, 3) # criando circulo

    # Adicionando texto centralizado
    text = COINS[i]
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)  # Obtém as dimensões do texto
    text_x = int(x - text_size[0] / 2)  # Calcula a coordenada x do ponto de início do texto para centralizá-lo
    text_y = int(y + text_size[1] / 2)  # Calcula a coordenada y do ponto de início do texto para centralizá-lo
    cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, COLOR, 2, cv2.LINE_AA)

cv2.imshow('Moedas', img)

cv2.waitKey(0)
cv2.destroyAllWindows()