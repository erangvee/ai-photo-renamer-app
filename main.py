from genname import generator

# Example usage with error handling
image_path = "./source/licensed-image.jpeg"
summary = generator.get_image_summary(image_path)
if summary:
    print(f"Image summary: {summary}")
else:
    print("Failed to generate image summary.")
