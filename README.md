# Indian Sign Language Translator 


## Project Overview
This project is a **Speech-to-Sign Language Translator** built using Streamlit, SpeechRecognition, and Pillow. It aims to bridge the communication gap between the hearing and speech-impaired community by converting spoken English into Indian Sign Language using GIFs or alphabet images. It also includes Text-to-Speech functionality.


## Features
- **Speech to Sign Language** : Recognizes your voice and translates it into ISL using relevant GIFs or alphabet images.
- **Text-to-Speech (TTS)**    : Converts typed text into spoken English using Google TTS.
- **ISL Dictionary**          : Downloadable PDF of Indian Sign Language resources.
- **Informative Videos**      : Embedded videos explaining ISL.
- **Modern UI**               : Styled using embedded CSS with orange/black color theme.


## Requirements

- Python 3.9+
- `streamlit`
- `speechrecognition`
- `pyaudio` *(for microphone access)*
- `gtts`
- `Pillow`


### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Application:

### Step 1: Navigate to the Project Directory

```bash
cd path\to\Indian_Sign_Language_Translator
```
### Replace path\to with your actual file path, for example:

```bash
cd F:\Projects\Indian_Sign_Language_Translator
```

### Step 2: Run the Streamlit App

```bash
python -m streamlit run Sign_Language.py
```

### Step 3: Open the Web App in a Browser
After successful execution, Streamlit will display a message like this in your terminal:

```bash
You can now view your Streamlit app in your browser.
Local URL: http://127.0.0.1:8501
Network URL: http://192.168.x.x:8501
```

Click the URL or copy and paste it into your browser:
🔗 http://127.0.0.1:8501
