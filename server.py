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

