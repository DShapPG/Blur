# import requests
# def detect_logo(image_bytes):
#     api_key="01QAbJLdr0UiqZHg83IP"
#     model_id="my-first-project-oar5a/2"
#     url = f"https://detect.roboflow.com/{model_id}?api_key={api_key}"

#     response = requests.post(
#         url,
#         files={"file": ("image.jpg", image_bytes, "image/jpeg")}
#     )

#     result = response.json()
#     return result
from ultralytics import YOLO
import cv2
import numpy as np

def detect_logo(image_bytes):
    # Загрузка модели
    model = YOLO("best.pt")  # путь к скачанному .pt файлу

    # Загрузка изображения
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Запуск инференса (детекция логотипов)
    result = model(image)[0]
    # Отображение результатов
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])
        class_id = int(box.cls[0])
    
    predictions = {x1, y1, x2, y2, confidence, class_id}
    return predictions
