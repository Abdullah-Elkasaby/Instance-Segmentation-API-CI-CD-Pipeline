import matplotlib.pyplot as plt
import matplotlib.patches as patches
from numpy import array, round 
from io import BytesIO
from base64 import b64encode


classes = [line.rstrip('\n') for line in open("dependencies/classes.txt")]



async def save_image(image, boxes, labels, scores, score_threshold=0.7):
    ratio = 800.0 / min(image.size[0], image.size[1])
    boxes /= ratio

    _, ax = plt.subplots(1, figsize=(12,9))
    image = array(image)
    ax.imshow(image)
    ax.axis('off')

    # Showing boxes with score > 0.7
    for box, label, score in zip(boxes, labels, scores):
        if score > score_threshold:
            rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=1, edgecolor='b', facecolor='none')
            ax.annotate(classes[label] + ':' + str(round(score, 2)), (box[0], box[1]), color='w', fontsize=12)
            ax.add_patch(rect)
    # tight to remove spaces around the image
    # plt.savefig(image_name, bbox_inches='tight')
    buffer = BytesIO()

    # Save the plot to the BytesIO stream
    plt.savefig(buffer, bbox_inches='tight', format='png')
    buffer.seek(0)
    return buffer

    
