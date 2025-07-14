import cv2
import numpy as np


def draw_rectangle(image_bytes, coordinates):
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    x1 = coordinates["x1"]
    x2 = coordinates["x2"]
    y1 = coordinates["y1"]
    y2 = coordinates["y2"]

    region = image[y1:y2, x1:x2]
    blurred_region = cv2.GaussianBlur(region, (151, 151), 0)
    image[y1:y2, x1:x2] = blurred_region
    #cv2.rectangle(image, (rectangle["x1"], rectangle["y1"]), (rectangle["x2"], rectangle["y2"]), (0, 0, 255), thickness=2)
    r_, img_encoded = cv2.imencode('.png', image)
    return img_encoded.tobytes()

