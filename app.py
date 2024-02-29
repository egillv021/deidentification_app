import streamlit as st
from deidentification.transform import TextTransformer

st.set_page_config(page_title="Deidentification", page_icon="🕵️‍♂️", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title('PII Masking App')

language_option = st.sidebar.radio(
    'Choose Language (select "Detect Language" for automatic detection):',
    ["Detect Language", "en", "de"],
    captions = ["", "English", "German"])

if "text_transformer" not in st.session_state:
# Initialize your TextTransformer
    st.session_state["text_transformer"]= TextTransformer()

col1, col2 = st.columns(2)
with col1:
    # Text input from user
    user_input = st.text_area("Enter Text Containing PII:", height=250)
    deidentify = st.button("Deidentify")
    masked_text = None
if deidentify:
    # Check if language detection is requested or a specific language is selected
    if language_option == 'Detect Language':
        # Language will be detected within the transform_text method
        masked_text = st.session_state["text_transformer"].transform_text(user_input)
    else:
        # Use the selected language
        masked_text = st.session_state["text_transformer"].transform_text(user_input, language=language_option)
with col2:
    # Displaying the masked text
    st.text_area("Masked Text:", value=masked_text, height=250, disabled=True)
