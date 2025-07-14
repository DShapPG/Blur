from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse, JSONResponse
import io
from ImageService import detect_logo

app = FastAPI()

@app.get("/")
def read_root():
    html = "ALO"
    return HTMLResponse(content = html)


@app.post("/image")
async def post_image(file: UploadFile = File(...)):
    # считываем присланные байты
    content = await file.read()
    detected_image = detect_logo(content)
    # отдаём их обратно потоком
    return JSONResponse(content=detected_image)
