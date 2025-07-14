import cv2
import numpy as np


def draw_rectangle(image_bytes, coordinates):
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    x = int(coordinates["predictions"][0]["x"])
    y = int(coordinates["predictions"][0]["y"] )
    width = int(coordinates["predictions"][0]["width"] )
    height = int(coordinates["predictions"][0]["height"] )
    rectangle = coordinates_convert(x,y,width,height)
    #cv2.rectangle(image, (rectangle["x1"], rectangle["y1"]), (rectangle["x2"], rectangle["y2"]), (0, 0, 255), thickness=2)
    blurred_image = blur(image, rectangle)
    r_, img_encoded = cv2.imencode('.png', blurred_image)
    return img_encoded.tobytes()

def coordinates_convert(x,y,width,height):
    x1 = int(x - width / 2)  # up left X
    y1 = int(y - height / 2)  # up left Y
    x2 = int(x + width / 2)  # bottom right X
    y2 = int(y + height / 2)  # bottom right Y
    rectangle = {"x1" : x1, "y1" : y1, "x2" : x2, "y2" : y2}
    return rectangle


def blur(image, area):
    region = image[area["y1"]:area["y2"],area["x1"]:area["x2"]]
    blurred_region = cv2.GaussianBlur(region, (151, 151), 0)
    image[area["y1"]:area["y2"],area["x1"]:area["x2"]] = blurred_region
    return image