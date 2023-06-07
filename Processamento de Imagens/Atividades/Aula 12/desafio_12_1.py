import cv2

video = cv2.VideoCapture('Processamento de Imagens/videos/IFMA Campus Caxias.mp4')

if not video.isOpened():
    print("Erro ao abrir o arquivo")

else:
    while video.isOpened():
        ret, frame = video.read()

        if ret is True:
            cannyConv = cv2.Canny(frame, 100, 200)
            cv2.imshow('Canny', cannyConv)

            k = cv2.waitKey(20)
            if k == 27:
                break
        
        else:
            break

video.release()
cv2.destroyAllWindows()