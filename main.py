from utils.preprocess import preprocess_image
from utils.dispaly import display_image
from onnxruntime import InferenceSession
import argparse


MODEL_PATH = "models/FasterRCNN-12-qdq.onnx"
session = InferenceSession(MODEL_PATH)









if __name__ == "__main__":
   
    image_path = ""
    org_img, img_data = preprocess_image(image_path)
    boxes, labels, scores = session.run(None, {session.get_inputs()[0].name: img_data})
    display_image(org_img, boxes, labels, scores)




