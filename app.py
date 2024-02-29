import streamlit as st
from deidentification.transform import TextTransformer

st.set_page_config(page_title="Deidentification", page_icon="🕵️‍♂️", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title('PII Masking App')

if "text_transformer" not in st.session_state:
# Initialize your TextTransformer
    st.session_state["text_transformer"]= TextTransformer()

# Allow the user to choose a language or opt for automatic detection
language_option = st.sidebar.selectbox(
    'Choose Language (select "Detect Language" for automatic detection):',
    ['Detect Language', 'en', 'de']  # Assuming 'en' and 'de' are the only supported languages for simplicity
)
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
