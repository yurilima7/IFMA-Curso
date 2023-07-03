import base64
import requests

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

image_path = "Processamento de Imagens/Yolo/test/Gemeos.jpg"
encoded_image = encode_image(image_path)

url = "http://localhost:8000/detect"

data = {
    "image": encoded_image
}

response = requests.post(url, json=data)

# Verificar o código de status da resposta
if response.status_code == 200:
    # Exibir a resposta JSON da API
    print(response.json())
else:
    print("Erro ao enviar solicitação POST:", response.status_code)
