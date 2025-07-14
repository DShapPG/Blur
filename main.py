from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
import io

app = FastAPI()

@app.get("/")
def read_root():
    html = "ALO"
    return HTMLResponse(content = html)


@app.post("/image")
async def post_image(file: UploadFile = File(...)):
    # считываем присланные байты
    content = await file.read()

    # отдаём их обратно потоком
    return StreamingResponse(
        io.BytesIO(content),              # превращаем bytes в «поток»
        media_type=file.content_type      # сохраняем исходный MIME-тип
    )