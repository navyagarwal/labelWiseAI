import streamlit as st

st.title("LabelWiseAI is here to help you eat right!")
uploaded_files = st.file_uploader(
    "Upload clear images of the food label.", type=['png', 'jpg'], accept_multiple_files=True
)

for uploaded_file in uploaded_files:
    st.image(uploaded_file)

