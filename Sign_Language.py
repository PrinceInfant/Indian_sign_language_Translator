import streamlit as st
import speech_recognition as sr
from PIL import Image
import os
import re
import string
import base64
import time
from gtts import gTTS


r = sr.Recognizer()

isl_gif = [
    'are you angry', 'are you hungry', 'be careful', 'do you have money',
    'do you want something to drink', 'good afternoon', 'good morning', 
    'good question', 'hello what is your name', 'i am fine', 'i am sorry', 
    'i am thinking', 'i go to a theatre', 'i love to shop',
    'please call me later', 'sit down', 'stand up', 'take care',
]

arr = list(string.ascii_lowercase)

def set_background(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    encoded_image = base64.b64encode(image_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            color: orange;
        }}
        h1, h2, h3, h4, h5, h6 {{ color: orange; }}
        .stButton button {{
            background-color: orange;
            color: black;
            border-radius: 8px;
            border: 2px solid black;
        }}
        .stButton button:hover {{
            background-color: #FF8C00;
            color:black;
            border-radius: 12px;
        }}
        .card {{
            background-color: rgba(86, 173, 199, 0.1);
            border-radius: 10px;
            padding: 30px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(230, 233, 238, 0.3);
        }}

        .card-icon {{
            font-size: 48px;
            color: #FFA500;
        }}

        .stDownloadButton > button {{
            background-color: orange;
            color: black;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
        .stDownloadButton > button:hover {{
            background-color: darkorange;
            color:black;
        }}
       .minimal-button {{
            background-color: transparent;
            border: none;
            color: #0366fc;  /* Blue color for the text */
            font-size: 18px;
            margin: 5px 0;
            text-align: left;
            cursor: pointer;
        }}

        .minimal-button:hover {{
            color: #1f77b4;  /* Slightly darker blue on hover */
            text-decoration: underline;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Listening...")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio).lower()
            st.success(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            st.error("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError:
            st.error("Request to Google API failed.")
    return None


def show_gif(text):
    gif_path = f'ISL_Gifs/{text}.gif'
    if os.path.exists(gif_path):
        gif_html = f'<img src="data:image/gif;base64,{read_gif(gif_path)}" width="300">'
        st.markdown(gif_html, unsafe_allow_html=True)
    else:
        st.error(f"No GIF found for: {text}")


def read_gif(gif_path):
    with open(gif_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


def show_letters(text):
    for char in text:
        if char in arr:  
            image_path = f'letters/{char}.jpg'
            if os.path.exists(image_path):
                placeholder = st.empty()
                with placeholder:  
                    img = Image.open(image_path)
                    st.image(img, width=240)
                time.sleep(1) 
                placeholder.empty() 
            else:
                st.error(f"Image not found for letter: {char}")

set_background("F:\Indian_sign_language\source_img\sign_language_bg.jpg")

if "page" not in st.session_state:
    st.session_state.page = "Home"  

def go_to_page(page_name):
    st.session_state.page = page_name


st.sidebar.header("Menu")

if st.sidebar.button("🏠 Home"):
    go_to_page("Home")

if st.sidebar.button("🌐 Translate"):
    go_to_page("Translate")

if st.sidebar.button("🗣️ Text to Speech"):
    go_to_page("Text to Speech")

if st.sidebar.button("🤟 About SL"):
    go_to_page("About SL")


if st.session_state.page == "Home":
    st.markdown("""<h1>Sign Language Translator</h1><br>""", unsafe_allow_html=True)
    st.image("F:\Indian_sign_language\source_img\signlang.png", width=350)
    st.write("")
    st.markdown(
        """
       <p>Break communication barriers with our cutting-edge Sign Language translation technology.
This innovative solution seamlessly converts sign language to text and speech, and vice versa.
Empowering individuals with diverse communication needs fosters inclusivity and understanding.
Join us in bridging the gap between signers and non-signers for a more connected world.Our user-friendly interface makes it easy for everyone to access and utilize this transformative technology.</p>
                """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.markdown("### Watch these informative videos about Sign Language:")
    st.write("")
    st.write("")
    def extract_video_id(url):
    
        regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
        match = re.search(regex, url)
        return match.group(1) if match else None


    video_links = [
        "https://youtu.be/qcdivQfA41Y?si=n1q94isitB8ZDprh",
        "https://youtu.be/vnH2BmcSRMA?si=_HZXMgHyWQMnIeZ9",
        "https://youtu.be/qtrBGmioR2Q?si=5XprSYYSu7FikSv8",
    ]

    cols = st.columns(len(video_links))

    for col, link in zip(cols, video_links):
        video_id = extract_video_id(link)
        if video_id:
            embed_link = f"https://www.youtube.com/embed/{video_id}"
            with col:
                st.markdown(
                    f'<iframe width="100%" height="180" src="{embed_link}" frameborder="0" allowfullscreen></iframe>',
                    unsafe_allow_html=True,
                )
        else:
            with col:
                st.error("Invalid YouTube link!")
    st.write("")
    video_links = [
        
        "https://youtu.be/XPRtZQSKL-4?si=jGk3YF4gsbRAGkhr", 
        "https://youtu.be/x58C6-ZtW_8?si=F7NAA2xpOeN8AbtL",
        "https://youtu.be/drs0_jcKr5w?si=94gL_5sdxZWHYysN",
    ]


    cols = st.columns(len(video_links))

    for col, link in zip(cols, video_links):
        video_id = extract_video_id(link)
        if video_id:
            embed_link = f"https://www.youtube.com/embed/{video_id}"
            with col:
                st.markdown(
                    f'<iframe width="100%" height="180" src="{embed_link}" frameborder="0" allowfullscreen></iframe>',
                    unsafe_allow_html=True,
                )
        else:
            with col:
                st.error("Invalid YouTube link!")    


elif st.session_state.page == "Translate":
    st.title("Speech to Sign Language")
    st.write("Translate your speech into ISL. Press the button to start recording.")
    if st.button("Start Recording"):
        recognized_text = recognize_speech()
        if recognized_text:
            if recognized_text in isl_gif:
                show_gif(recognized_text)
            else:
                show_letters(recognized_text)
           

elif st.session_state.page == "Text to Speech":
    st.title("Text-to-Speech Converter")
    text_input = st.text_area("", height=150)
    if st.button("Convert to Speech"):
        if text_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            try:
                tts = gTTS(text=text_input, lang='en', slow=True)
                tts.save("output.mp3")
                st.success("Speech generated successfully!")
                audio_file = open("output.mp3", "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
            except Exception as e:
                st.error(f"An error occurred: {e}")


elif st.session_state.page == "About SL":
    st.header("ISL Translator Features")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="card">
                <div class="card-icon">💬</div>
                <h2 class="title">Text-to-Speech</h2>
                <p>Our Text-to-Speech feature seamlessly converts translated text into spoken language, enhancing communication for both signers and non-signers in an effective and easy way.</p>
               
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <div class="card-icon">📚</div>
                <h2 class="title">Dictionary</h2>
                <p>Access a comprehensive dictionary of Indian Sign Language signs, complete with descriptions and video demonstrations and provides an extensive collection of Indian Sign Language signs.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
                <div class="card-icon">🌐</div>
                <h2 class="title">Speech to Sign language</h2>
                <p>By utilizing advanced speech recognition technology, accurate translations, making interaction across linguistic communities.</p>
                
            </div>
        """, unsafe_allow_html=True)
    st.write("")
    st.write("")
    pdf_file_path = "F:\Indian_sign_language\pdf.pdf"

    with open(pdf_file_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()

    st.title("Download Dictionary")

    st.markdown("Click the button below to download the PDF dictionary.")


    st.download_button(
        label="Download Dictionary PDF", 
        data=pdf_data,  
        file_name="dictionary.pdf", 
        mime="application/pdf", 
        key="download_pdf"  
    )