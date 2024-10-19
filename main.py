from dotenv import load_dotenv
import base64
import json
import os

import google.generativeai as genai

def get_image_summary(path):
    load_dotenv('.secrets')
    api_key = os.getenv('GOOGLE_API_KEY')

    # Configure API client
    genai.configure(api_key=api_key)

    # Configure model
    model_name = "gemini-1.5-flash"
    model = genai.GenerativeModel(model_name=model_name)

    generation_config = {
        "temperature": 0.4,
        "top_k": 32,
        "top_p": 1,
        "max_output_tokens": 4096,
    }

    # Set safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

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
        response = model.generate_content(contents=[prompt], generation_config=generation_config, safety_settings=safety_settings)
        
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
