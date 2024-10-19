from dotenv import load_dotenv
import base64
import json
import os

import google.generativeai as genai

def get_image_summary(path):
    load_dotenv('.secrets')
    api_key = os.getenv('GOOGLE_API_KEY')

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Configure API client
    genai.configure(api_key=api_key)

    # Load and encode image data
    try:
        with open(path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
            print(f"Image data encoded: {len(image_data)} characters")  # Check encoding length
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        return

    # Create prompt with Base64 encoded image data
    prompt = {
        "role": "user",
        "parts": [
            {
                "text": "Write a one sentence short summary of this image. The sentence should be no more than five words."
            },
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_data
                }
            }
        ]
    }

    # Generate the response using the model
    try:
        response = model.generate_content(contents=[prompt])
        
        return response._result.candidates[0].content.parts[0].text.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return

# Example usage with error handling
image_path = "./source/licensed-image.jpeg"
summary = get_image_summary(image_path)
if summary:
    print(f"Image summary: {summary}")
else:
    print("Failed to generate image summary.")
