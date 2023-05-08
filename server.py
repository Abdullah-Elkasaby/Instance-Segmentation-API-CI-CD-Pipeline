# FASTAPI Imports
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import json
import uvicorn
from uuid import uuid4

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
    org_img, boxes, labels, scores = await run_inference(img.file)
    imag_ext = img.filename.split('.')[1]
    rand_image_name = f"{uuid4()}.{imag_ext}"
    await save_image(rand_image_name, org_img, boxes, labels, scores)

    return FileResponse(rand_image_name)




if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")