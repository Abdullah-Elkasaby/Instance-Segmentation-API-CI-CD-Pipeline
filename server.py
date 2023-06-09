# FASTAPI Imports
from fastapi import FastAPI, UploadFile,File, HTTPException
from fastapi.responses import Response, HTMLResponse


# Model Imports
from utils.preprocess import preprocess_image
from utils.postprocess import save_image
from onnxruntime import InferenceSession

app = FastAPI()
MODEL_PATH = "models/FasterRCNN-12-qdq.onnx"
session = InferenceSession(MODEL_PATH)


async def run_inference(image_path):
    org_img, img_data = await preprocess_image(image_path)
    boxes, labels, scores =  session.run(None, {session.get_inputs()[0].name: img_data})
    return (org_img, boxes, labels, scores)




@app.post("/upload")
async def create_upload_file(img: UploadFile = File(...)):
    try:
        org_img, boxes, labels, scores = await run_inference(img.file)
    
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error [Bad Inference]")

    image = await save_image(org_img, boxes, labels, scores)

    return Response(content=image.getvalue(), media_type="image/png")




@app.get("/home")
async def index():
    html_file_path = "index.html"

    with open(html_file_path, "r") as file:
        contents = file.read()

    return HTMLResponse(content=contents, status_code=200)

