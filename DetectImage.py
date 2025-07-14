import requests
def detect_logo(image_bytes):
    api_key = "01QAbJLdr0UiqZHg83IP"
    model_id = "logodet-3k-a6lrf/1"
    url = f"https://detect.roboflow.com/{model_id}?api_key={api_key}"

    response = requests.post(
        url,
        files={"file": ("image.jpg", image_bytes, "image/jpeg")}
    )

    result = response.json()
    return result