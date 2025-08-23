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
custom_st_style = """
    <style>
    #MainMenu {visibility: hidden;}     /* Hides the hamburger menu */
    header {visibility: hidden;}       /* Hides the header */
    footer {visibility: hidden;}       /* Hides the default footer */
    
    /* Add custom footer */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117; /* dark background */
        color: #fafafa;            
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #444;
        z-index: 100;
    }

    .custom-footer a {
        color: #61dafb; /* link color (light blue) */
        text-decoration: none;
        margin: 0 8px;
    }

    .custom-footer a:hover {
        text-decoration: underline;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .custom-footer {
            font-size: 12px;
            padding: 8px;
        }
    }

    @media (max-width: 480px) {
        .custom-footer {
            font-size: 11px;
            padding: 6px;
        }
    }
    </style>

    <div class="custom-footer">
        Built by <b>Goodnews</b> © 2025 | Powered with ❤️ by Streamlit <br>
        <a href="https://github.com/yourusername" target="_blank">GitHub</a> |
        
    </div>
"""
st.markdown(custom_st_style, unsafe_allow_html=True)
