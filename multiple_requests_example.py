import requests
import concurrent.futures
import random
url = "http://ad8eee7dc738f4a9fbca72a9e305c1dc-1311341917.us-east-2.elb.amazonaws.com/upload"
num_requests = 50
image_file = "dependencies/demo.jpg"

def send_request(url, image_file):
    with open(image_file, "rb") as file:
        files = {"img": file}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            # Extract the filename from the URL
            filename = url.split("/")[-1]
            # Save the image to a file
            with open(filename + f"{random.randint(1,1000)}.png", "wb") as file:
                file.write(response.content)
            return f"Image saved: {filename}"
        else:
            return f"Failed to retrieve image from: {url}"

    # Process the response as needed
    return response.text

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_request, url, image_file) for _ in range(num_requests)]
    concurrent.futures.wait(futures)

    for future in futures:
        try:
            result = future.result()
            # Process the result as needed
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
