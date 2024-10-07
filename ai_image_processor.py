import requests
import cv2
import numpy as np
from PIL import Image
import io
import time
import sys
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("MY_API_KEY")

def download_image(url):
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))

def detect_faces(image):
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def generate_image(prompt, retries=3, delay=5):
    api_url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"inputs": prompt}
    
    for attempt in range(retries):
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            try:
                return Image.open(io.BytesIO(response.content))
            except Exception as e:
                raise ValueError("Failed to decode image from response") from e
        elif response.status_code == 503:
            print(f"Service unavailable (503). Retrying in {delay} seconds...")
            time.sleep(delay)
        else:
            raise ValueError(f"API request failed with status code {response.status_code} and message: {response.text}")
    raise ValueError("Max retries exceeded. API service is unavailable.")

def generate_post_content(prompt):
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"inputs": prompt}
    
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        raise ValueError(f"API request failed with status code {response.status_code} and message: {response.text}")

def create_social_post(image_source, user_prompt):
    # Load and process image
    if image_source.startswith(('http://', 'https://')):
        image = download_image(image_source)
    else:
        image = Image.open(image_source)
    
    # Detect faces
    faces = detect_faces(image)
    print(f"Detected {len(faces)} faces in the image.")
    
    # Generate new image based on user prompt
    generated_image = generate_image(user_prompt)
    generated_image.save("generated_image.jpg")
    print("Generated image saved as 'generated_image.jpg'")
    
    # Generate post content
    post_content = generate_post_content(user_prompt)
    print("Generated post content:", post_content)
    
    # Create a mock social media post
    social_post = {
        "user_image": image_source,
        "generated_image": "generated_image.jpg",
        "post_content": post_content,
        "likes": 0,
        "comments": []
    }
    
    # Save the post as JSON
    with open("social_post.json", "w") as f:
        json.dump(social_post, f, indent=2)
    print("Social post data saved as 'social_post.json'")
    
    return social_post

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ai_social_content_generator.py <image_source> <user_prompt>")
        sys.exit(1)
    
    image_source = sys.argv[1]
    user_prompt = sys.argv[2]
    
    social_post = create_social_post(image_source, user_prompt)
    print("Social post created successfully!")

# Example usage:
# python ai_social_content_generator.py face.jpg "Create a futuristic cityscape for my profile"
# or
# python ai_social_content_generator.py https://www.pexels.com/photo/man-in-brown-polo-shirt-614810/ "Generate an inspirational quote about technology"