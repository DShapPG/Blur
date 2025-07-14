from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse, JSONResponse
import io
from DetectImage import detect_logo
from BlurImage import draw_rectangle

app = FastAPI()

@app.get("/")
def read_root():
    html = "ALO"
    return HTMLResponse(content = html)


@app.post("/image")
async def post_image(file: UploadFile = File(...)):
    try:
        content = await file.read()
        image_info = detect_logo(content)
        # if not image_info or not all(k in image_info for k in ("x1", "y1", "x2", "y2")):
        #     return JSONResponse(content={"error": "Logo wasn't found"}, status_code=400)
        rectangle = draw_rectangle(content, image_info)
        return StreamingResponse(io.BytesIO(rectangle), media_type="image/png")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
