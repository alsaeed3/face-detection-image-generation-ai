# AI Image Processor

This project detects faces in images and generates new images based on text prompts.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Make the virtual environment for python:
   ```sh
   On Linux/Mac: python3 -m venv <your_virtual_environment_name>
   On Windows: python -m venv <your_virtual_environment_name>
   ```

3. Activate your Virtual Environment:
   ```sh
   source <your_virtual_environment_name>/bin/activate
   ```
4. Install the required dependencies:
   ```sh
   On Linux/Mac: pip3 install -r requirements.txt
   On Windows: pip install -r requirements.txt
   ```

5. Create a `.env` file and add your API key:
   ```env
   MY_HF_API_KEY=your_hf_api_key_here
   ```

## Usage

To generate a social media post with an image and text prompt, run the following command:
```sh
On Linux/Mac: python3 ai_image_processor.py <image_source> <user_prompt>
On Windows: python ai_image_processor.py <image_source> <user_prompt>
```
- `<image_source>`: Path to a local image file or a URL to an image.
- `<user_prompt>`: Text prompt to generate a new image.

Example:
```sh
On Linux/Mac: python3 ai_image_processor.py face.jpg "Create a futuristic cityscape for my profile"
On Windows: python ai_image_processor.py face.jpg "Create a futuristic cityscape for my profile"
```
or
```sh
On Linux/Mac: python3 ai_image_processor.py https://www.pexels.com/photo/man-in-brown-polo-shirt-614810/ "Generate an inspirational quote about technology"
On Windows: python ai_image_processor.py https://www.pexels.com/photo/man-in-brown-polo-shirt-614810/ "Generate an inspirational quote about technology"
```

## Functions

### `download_image(url)`
Downloads an image from the given URL.

### `detect_faces(image)`
Detects faces in the provided image.

### `generate_image(prompt, retries=3, delay=5)`
Generates a new image based on the text prompt.

### `generate_post_content(prompt)`
Generates content for a social media post based on the text prompt.

### `create_social_post(image_source, user_prompt)`
Creates a social media post by processing the image and generating content based on the user prompt.

## Example

To create a social media post, you can use the following command:
```sh
On Linux/Mac: python3 ai_image_processor.py face.jpg "Create a futuristic cityscape for my profile"
On Windows: python ai_image_processor.py face.jpg "Create a futuristic cityscape for my profile"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.