import streamlit as st
from utility.helper_functions import ocr_foodlabel, images_to_pdf
from PIL import Image

st.title("LabelWiseAI is here to help you eat right!")
uploaded_files = st.file_uploader(
    "Upload clear images of the food label.", type=['png', 'jpg'], accept_multiple_files=True
)

process_label_button = st.button("Process Label", disabled=(not uploaded_files))

if process_label_button and uploaded_files:
    images = [Image.open(image) for image in uploaded_files]
    pdf_file = images_to_pdf(images)
    text = ocr_foodlabel(pdf_file)
    st.write(text)

if uploaded_files is None:
    st.warning("Please upload a file to enable the 'Process Label' button.")

for uploaded_file in uploaded_files:
    st.image(uploaded_file)