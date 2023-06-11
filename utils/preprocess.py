import numpy as np
from PIL import Image
from math import ceil

async def preprocess_image(image_path):
    # Resize
    with Image.open(image_path) as org_image:
        image = org_image.copy()
        ratio = 800.0 / min(image.size[0], image.size[1])
        image = image.resize((int(ratio * image.size[0]), int(ratio * image.size[1])), resample=Image.BILINEAR)

    # Convert to BGR
    image = np.array(image)[:, :, [2, 1, 0]].astype('float32')

    # HWC -> CHW
    image = np.transpose(image, [2, 0, 1])

    # Normalize
    mean_vec = np.array([102.9801, 115.9465, 122.7717], dtype=np.float32)
    image -= mean_vec[:, np.newaxis, np.newaxis]

    # Pad to be divisible by 32
    padded_h = int(ceil(image.shape[1] / 32) * 32)
    padded_w = int(ceil(image.shape[2] / 32) * 32)

    padded_image = np.zeros((3, padded_h, padded_w), dtype=np.float32)
    padded_image[:, :image.shape[1], :image.shape[2]] = image
    image = padded_image

    return org_image, image
