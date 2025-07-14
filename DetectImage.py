
from ultralytics import YOLO
import cv2
import numpy as np

def detect_logo(image_bytes):

    model = YOLO("best.pt")
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = model(image)[0]

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])
        class_id = int(box.cls[0])
    
    predictions = {"x1" : x1, "y1" : y1, "x2" : x2, "y2" : y2, "confidence" : confidence, "class_id" : class_id}
    return predictions
