# Instance Segmentation API Using FasterRCNN in ONNX format using FastAPI

## Introduction

This documentation provides an overview of the Instance Segmentation API project. The project aims to serve an instance segmentation model called FasterCNN using the FastAPI framework. The model is based on the ONNX framework and the API utilizes async functionality for improved performance.

## Project Components

The project consists of the following components

- Instance Segmentation Model: The model used for instance segmentation is FasterCNN. It is an efficient convolutional neural network       (CNN) architecture capable of detecting and segmenting instances in an image.

- FastAPI: FastAPI is a high-performance web framework for building APIs with Python. It is used to create the API endpoint that serves the instance segmentation model.

- ONNX: ONNX (Open Neural Network Exchange) is an open format for representing deep learning models. The FasterCNN model is based on the ONNX framework, allowing easy interoperability with various deep learning frameworks.

- Async: The project utilizes async functionality, which enables asynchronous execution of tasks. This improves the performance of the API by allowing multiple requests to be processed concurrently.

## API Endpoint

The project exposes a single endpoint for performing instance segmentation on images. The endpoint accepts HTTP POST requests with an image file or image URL as input.

### Endpoint URL

The base URL for the API endpoint is: `http://127.0.0.1:8000/docs` ,however you can change that as you see fit.

### Request Format

The API endpoint expects a JSON payload in the body of the POST request. The payload should include the following fields:

- `"image"` (required): The input image to be segmented. It can be either an image file (JPEG, PNG, etc).
e confidence scores associated with each instance segmentation.


## Setup and Deployment

To set up and deploy the Instance Segmentation API project, follow these steps:

1. Create a virtual enviroment 
    * `python -m venv venv`

2. Activate the virtual enviroment 
    * on windows use `./venv/Scripts/activate`
    * on linux use `source venv/Scripts/bin`

3. Install the required dependencies, including FastAPI, ONNX, and any other necessary libraries.
    * `pip install -r requirements.txt`

4. Run the FastAPI server using Uvicorn after opening the directory containgy the `server.py` file 
    * `uvicorn server:app  --host 0.0.0.0 --port 8000`

<br>

## Usage Example 
![image](dependencies/usage.png)

## Conclusion

The Instance Segmentation API project provides a simple and efficient way to perform instance segmentation on images using the FasterCNN model. By leveraging FastAPI, ONNX, and async functionality.
