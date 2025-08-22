import streamlit as st
from googletrans import Translator

# Translator instance
translator = Translator()

# Streamlit app
st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌍 Language Translator App")

# User input
text_to_translate = st.text_area("Enter text to translate:", "")

# Choose target language
languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Yoruba": "yo",
    "Igbo": "ig",
    "Hausa": "ha"
}

target_lang = st.selectbox("Choose target language:", list(languages.keys()))

if st.button("Translate"):
    if text_to_translate.strip():
        translated = translator.translate(text_to_translate, dest=languages[target_lang])
        st.success(f"**Translation in {target_lang}:**\n\n{translated.text}")
    else:
        st.warning("⚠️ Please enter some text to translate.")
