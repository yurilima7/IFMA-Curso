import cv2

cap = cv2.VideoCapture('Processamento de Imagens/videos/IFMA Campus Caxias.mp4')

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # largura do vídeo
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # altura do vídeo

if not cap.isOpened():
    print("Erro ao acessar")
else:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Input', frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Gray', gray)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        if cv2.waitKey(20) & 0xFF == ord('w'):
            print("Salvando frame...")
            cv2.imwrite('Processamento de Imagens/images/print.jpg',frame)
            cv2.imwrite('Processamento de Imagens/images/gray.jpg',gray)

cap.release()
cv2.destroyAllWindows()