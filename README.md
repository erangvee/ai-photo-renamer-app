# AI Photo Renamer (Gemini)
This application uses [Gemini Developer API](https://ai.google.dev/). The development process is inspired by the following:

* [Using Generative AI to Improve Image Filenames](https://www.raymondcamden.com/2024/01/26/using-generative-ai-to-improve-image-filenames)
* [ai-photo-renamer](https://github.com/philspaceagency/ai-photo-renamer)

The intention is to use [Streamlit](https://streamlit.io/) to deploy the AI Photo Renamer to the web for practical use. (Streamlit development ongoing as of 19 October 2024.)

This code feeds on images inside the `/source` folder, generates a filename based on the image (using Gemini `gemini-1.5-flash` model), and copies and renames the images to `/output`.

# Python Environment
This code is developed and tested on Python 12. Packages used with their corresponding versions are in `requirements.txt`.

# Instructions
1. Grab your API Key from [Google AI Studio](https://aistudio.google.com/).
2. In root, create a `.secrets` file.
3. Inside the `.secrets` file, add your API key in the format:
```
GOOGLE_API_KEY=YOUR_API_KEY
```
4. Run `streamlit run "Photo Renamer.py"`

