from ultralytics import YOLO
import cv2

model = YOLO("Processamento de Imagens/Yolo/train/best.pt")
image_path = "Processamento de Imagens/Yolo/leon.jpg"
image = cv2.imread(image_path)

# Fazendo a classificação
results = model.predict(source=image_path, save=False, imgsz=640, conf=0.7)
height, width, channels = image.shape

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.9
thickness = 2

# Obtendo os nomes das classes
class_names = model.names

if len(results[0].boxes.data) > 0:
    # Obtendo os resultados das detecções
    detections = results[0].boxes.data[0].numpy()

    # Armazenando as coordenadas
    x_min, y_min, x_max, y_max, conf, cls_index = detections

    # Verificado a classe detectada
    class_name = class_names[cls_index]
    print("Classe: {}".format(class_name))

    # Messagem de retorno
    message = f"{class_name}: {conf * 100:.2f}%"
    text_width, _ = cv2.getTextSize(message, fontFace, fontScale, thickness)

    x = int((width - text_width[0]) / 2)

    # Desenhar as bounding boxes na imagem
    cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
    cv2.putText(image, message, (x , int(height) - 10), fontFace, fontScale, (0, 255, 255), thickness)

    # Exibir a imagem com as bounding boxes
    cv2.imshow("Constelacao", image)

else: 
    print('Nada detectado')

cv2.waitKey(0)
cv2.destroyAllWindows()