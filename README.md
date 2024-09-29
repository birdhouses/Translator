# AI Translator

## Overview

This project is a Streamlit web application that provides AI-powered translation of uploaded CSV or text files. Users can select source and target languages, upload files, and download the translated text. The application uses a custom module, `Translator`, which interfaces with an AI language model to perform translations.

## Features

- **File Upload**: Supports CSV, TXT, and Markdown file uploads.
- **Language Detection and Translation**: Automatically detects or allows the user to select the source language. Users can choose the target language.
- **Progress Feedback**: Displays a progress bar and status while translating.
- **Translation Download**: Allows users to download the translated text as a file.
- **Streamlit Interface**: Provides a simple web-based UI to interact with the translator.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/birdhouses/Translator.git
   cd Translator
   ```

2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the root directory with the following content:

     ```
     OPENAI_API_KEY=your_openai_api_key
     OPENAI_ASSISTANT_ID=your_assistant_id
     ```

4. Run the application:

   ```sh
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit application in your browser.
2. Upload a CSV or text file that you want to translate.
3. Select the source language (or choose "Detect Language").
4. Select the target language for translation.
5. Enter a model name if you want to use a custom model (default is "gpt-4o-mini").
6. Click the **Translate** button.
7. Download the translated file or view the translated text in the text area.

## Modules

### `app.py`

The main entry point for the Streamlit app. It handles:

- File uploads.
- Language selection.
- Calling the `Translator` module for translation.
- Displaying progress and results to the user.

### `modules/translator.py`

Contains the `Translator` class, which handles the text translation using an AI model:

- Splits the input text into manageable chunks for translation.
- Interacts with the `Assistant` class to obtain translated results.
- Provides progress feedback during translation.

### `modules/assistant.py`

Implements the `Assistant` class, which interacts with the OpenAI API:

- Handles the conversation with the assistant.
- Retrieves the translated text.
- Manages tool calls and progress updates.

## Dependencies

- `streamlit`: Used for creating the web UI.
- `pandas`: For handling CSV files.
- `tiktoken`: To tokenize text for input to the AI model.
- `openai`: To communicate with the OpenAI API.
- `python-dotenv`: For loading environment variables from a `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- This project uses OpenAI's language models for translations.
- Streamlit is used to create the user interface for easy interaction.

## Contributing

Feel free to fork the repository and submit pull requests. Any contributions to improve this project are welcome!