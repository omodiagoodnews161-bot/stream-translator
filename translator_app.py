import streamlit as st
from deep_translator import GoogleTranslator

# Title
st.title("🌍 Multi-Language Translator App")

# Input text
text = st.text_area("Enter text to translate:")

# Language selection
languages = {
    "English": "en", "French": "fr", "Spanish": "es", "German": "de", 
    "Italian": "it", "Chinese (Simplified)": "zh-CN", "Japanese": "ja",
    "Arabic": "ar", "Russian": "ru", "Portuguese": "pt"
}

source_lang = st.selectbox("Select source language:", list(languages.keys()))
target_lang = st.selectbox("Select target language:", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang], 
                target=languages[target_lang]
            ).translate(text)
            
            st.success(f"**Translated Text ({target_lang}):** {translated}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text first.")
