import streamlit as st
from google.cloud import documentai
from google.oauth2 import service_account
import io

project_id = st.secrets["PROJECT_ID"]
location = st.secrets["LOCATION"]
processor_id = st.secrets["PROCESSOR_ID"]
processor_version = st.secrets["PROCESSOR_VERSION"]

cred = service_account.Credentials.from_service_account_info(
    st.secrets['GOOGLE_APPLICATION_CREDENTIALS']
)
client = documentai.DocumentProcessorServiceClient(credentials=cred)

def images_to_pdf(images):
    pdf_buffer = io.BytesIO()
    images[0].save(pdf_buffer, save_all=True, append_images=images[1:], format="PDF")
    pdf_buffer.seek(0)
    return pdf_buffer

def ocr_foodlabel(pdf_file):
    if pdf_file is not None:
        content = pdf_file.read()

    raw_document = documentai.RawDocument(
        content=content,
        mime_type="application/pdf",
    )
    processor_name = client.processor_version_path(
        project_id, location, processor_id, processor_version
    )

    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    return document.text