import cv2

total_pessoas = 0
cap = cv2.VideoCapture('Processamento de Imagens/videos/IFMA Campus Caxias.mp4')

face_cascade = cv2.CascadeClassifier('Processamento de Imagens/classificadores/haarcascade_frontalface_default.xml')

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    ret, frame = cap.read()

    
    # Verificando se a leitura do quadro foi bem-sucedida
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Contando o número de pessoas
    total_pessoas = len(faces)

    # Exibe o número de pessoas na imagem do vídeo
    cv2.putText(frame, f'Pessoas: {total_pessoas}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    cv2.imshow('Video', frame)

    c = cv2.waitKey(20)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
