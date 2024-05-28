import streamlit as st
from translator_utils import translate

st.set_page_config(
    page_title="Translator.AI",
    page_icon="🈶",
    layout="centered"
)

# streamit page title
st.title("🈶 Translator App  - GPT-4o")

col1, col2 = st.columns(2)

with col1:
    input_languages_list = ["English", "French", "German", "Latin", "Spanish", "Hindi", "Tamil", "Telugu", "Marathi"]
    input_language = st.selectbox(label="Input Language", options=input_languages_list)

with col2:
    output_languages_list = [x for x in input_languages_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_languages_list)

input_text = st.text_area("Type the text to be translated")

if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)
    st.success(translated_text)
