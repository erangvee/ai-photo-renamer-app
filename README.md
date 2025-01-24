# AI Photo Renamer (Gemini)
This application uses [Gemini Developer API](https://ai.google.dev/). The development process is inspired by the following:

* [Using Generative AI to Improve Image Filenames](https://www.raymondcamden.com/2024/01/26/using-generative-ai-to-improve-image-filenames)
* [ai-photo-renamer](https://github.com/philspaceagency/ai-photo-renamer)

The intention is to use [Streamlit](https://streamlit.io/) to build an AI Photo Renamer that can be deployed to the web for practical use.

In this application, the user can upload images, which the application will store in a `/source-<randomhash>` folder. The code feeds on images inside the `/source-<randomhash>` folder, generates a filename based on the image/s (using Gemini `gemini-1.5-flash` model), and copies and renames the image/s to `/output-<randomhash>`.

The user can download the new generated files compressed into ZIP files.

# Other info
* To facilitate simultaneous use of the Streamlit app, unique `source` and `output` folders are created per session to separate images uploaded by different users. 
* The `source` and `output` folders are deleted after session is finished (requires the user to click Finished Session button). At the same time, a new function is added such that every time someone accesses the web app, it checks if there are existing session files older than 1 hour and deletes them.
* If an image similar to a processed one is named similarly, the filename is appended with a counter (i.e. `hand-holds-city-polaroid-photo.png`, `hand-holds-city-polaroid-photo (1).png`, `hand-holds-city-polaroid-photo (2).png`, ...)
* The prompt requires the image description (which is used as new filename) to be no more than 5 words. You can update the base prompt in `vars`.
* The prompt can be modified by the end user by appending to it only. The app has the option to append additional text to the original prompt.
* For further development:
    * Reset prompts to original.
    * Give options for prompts.

# To fix
* The processing restarts every time the download button is clicked.

# `vars` file
The `vars` file is used to specify variables that you can quickly modify without having to scour through the source code. Here are what the variables for:

* `PAGE_TITLE`: Name of the web app. This will show in the window/tab name of the browser and at the top of the page.
* `PAGE_DESC`: This text will show up at the start of the page.
* `FAVICON`: Path of the image to be used as favicon.
* `LAYOUT`: How the streamlit app will render. It can be `wide` and `centered`. (See [st.set_page_config](https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config))
* `SOURCE_PREFIX`: Prefix for the source directory. By default: `source-`
* `OUTPUT_PREFIX`: Prefix for the output directory. By default: `output-`
* `GEMINI_VER`: Just a text to show end users what Gemini model version is currently used.
* `HOURS_OLD`: The app will delete session files older than what's set here.
* `BASE_PROMPT`: Base prompt used in the application.

# Python Environment
This code is developed and tested on Python 12. Packages used with their corresponding versions are in `requirements.txt`.

# Instructions
1. Grab your API Key from [Google AI Studio](https://aistudio.google.com/).
2. In root, create a `.secrets` file.
3. Inside the `.secrets` file, add your API key in the format:
```
GOOGLE_API_KEY=YOUR_API_KEY
```
4. Configure other page settings in `vars`.
5. Run `streamlit run "Photo Renamer.py"`

