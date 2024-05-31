# youtube-kid-safe-check
Youtube AI Kid Safe Checker

# YouTube Video Transcript Analysis for Kids

This Streamlit application fetches the transcript of a YouTube video, checks for any filthy or bad words, and evaluates if the content is suitable for kids using the semantic model `all-MiniLM-L6-v2`.

## Features

- Fetch transcript of a YouTube video using the video ID or link.
- Check for the presence of any predefined naughty words.
- Perform semantic analysis to determine if the content is appropriate for kids.
- Display results indicating whether the video is suitable for kids.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/senthilthangaiah/youtube-kid-safe-check.git
    cd youtube-kid-safe-check
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.streamlit` directory and add `config.toml` for Streamlit configuration (optional).

## Usage

1. Add your list of naughty words to `input.csv`. The CSV should have a single column named `word`.

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open the application in your browser. Enter the YouTube video ID or link to analyze the transcript.

## Code Overview

### `app.py`

This is the main script that runs the Streamlit application. It includes the following functionalities:

- Load list of naughty words from `input.csv`.
- Load the `all-MiniLM-L6-v2` model for semantic analysis.
- Fetch the YouTube video transcript using `youtube-transcript-api`.
- Check for naughty words in the transcript.
- Perform semantic analysis to determine if the content is suitable for kids.
- Display results and the transcript in the Streamlit app.

### `input.csv`

This file contains a list of naughty words to check against the transcript. It should have a single column named `word`.

### `.streamlit/config.toml`

(Optional) Streamlit configuration file. Example content:
```toml
[server]
headless = true
port = 8501
enableCORS = false
```
### Example
To test the application, run the following command:

```bash
streamlit run app.py
```

Enter a YouTube video ID or link in the text input field and click enter. The application will fetch the transcript and analyze it for any naughty words or adult content.

### Results.

# Changes Required
![screenshot]()

### License
This project is licensed under the MIT License. See the LICENSE file for details.

css
Copy code

### `requirements.txt`

Make sure to create a `requirements.txt` file to list all the dependencies:

```streamlit
youtube-transcript-api
pandas
sentence-transformers
torch
transformers
```
