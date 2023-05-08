from utils.preprocess import preprocess_image
from utils.dispaly import display_image
from onnxruntime import InferenceSession
import argparse


MODEL_PATH = "models/FasterRCNN-12-qdq.onnx"
session = InferenceSession(MODEL_PATH)





parser = argparse.ArgumentParser(description="perform instance segementation on an image using fasterRCNN")


if __name__ == "__main__":
    usage = parser.format_usage()
    usage = usage.replace("usage:", "Usage: python script.py --image_path")
    parser.usage = usage
    parser.add_argument("image_path", help="path to the image")
    args = parser.parse_args()
    image_path = args.image_path
    org_img, img_data = preprocess_image(image_path)
    boxes, labels, scores = session.run(None, {session.get_inputs()[0].name: img_data})
    display_image(org_img, boxes, labels, scores)




