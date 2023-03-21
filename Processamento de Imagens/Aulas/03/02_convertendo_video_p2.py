import cv2
cap = cv2.VideoCapture("Processamento de Imagens/videos/IFMA Campus Caxias.mp4")

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # largura do vídeo
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # altura do vídeo
fps = cap.get(cv2.CAP_PROP_FPS) # valor de frame por segundo

if not cap.isOpened():
    print("Erro ao acessar a câmera")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("Processamento de Imagens/videos/video_cinza.avi", 
                             fourcc, int(fps), (int(frame_width), int(frame_height)), False)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output.write(gray)

        cv2.imshow('Cinza', gray)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        if cv2.waitKey(20) & 0xFF == ord('w'):
            print("Salvando frame...")
            cv2.imwrite('Processamento de Imagens/images/print.jpg',gray)

cap.release()
output.release()
cv2.destroyAllWindows()