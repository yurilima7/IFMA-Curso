import numpy as np
import cv2

img = cv2.imread('Processamento de Imagens/images/palhaco.png', 0)

# Calcula a transformada de Fourier
dft = np.fft.fft2(img)

# Shifta o espectro para centralizar as baixas frequências
dft_shift = np.fft.fftshift(dft)

# Calcula a magnitude do espectro de Fourier
magnitude_spectrum = np.log(np.abs(dft_shift)) / 20

# raio do filtro
radius = 32

mask = np.zeros_like(img)
cy = mask.shape[0] // 2
cx = mask.shape[1] // 2

cv2.rectangle(mask, (cx-45,0), (cx-20,cy*2), (255,255,255), -1)
cv2.rectangle(mask, (cx+20,0), (cx+45,cy*2), (255,255,255), -1)

mask = 255 - mask
mask = cv2.GaussianBlur(mask, (9, 9), 0)

dft_shift_masked = np.multiply(dft_shift, mask) / 255
back_ishift = np.fft.ifftshift(dft_shift)
back_ishift_masked = np.fft.ifftshift(dft_shift_masked)

img_filtered = np.fft.ifft2(back_ishift_masked)
img_filtered = np.abs(img_filtered).clip(0, 255).astype(np.uint8)

cv2.imshow("Imagem", img)
cv2.imshow("Espectro", magnitude_spectrum)
cv2.imshow("Mascara", mask)
cv2.imshow("Resultado", img_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
