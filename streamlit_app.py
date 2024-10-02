import streamlit as st
from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from google.oauth2 import service_account

st.title("LabelWiseAI is here to help you eat right!")
uploaded_file = st.file_uploader(
    "Upload clear images of the food label.", type=['png', 'jpg']
)

# , accept_multiple_files=True

# for uploaded_file in uploaded_files:
#     st.image(uploaded_file)

project_id = "labelwiseai"
processor_display_name = "entityextractor4"

def quickstart(project_id: str, processor_display_name: str = "My Processor",):
    # opts = ClientOptions(credentials_file=st.secrets['GOOGLE_APPLICATION_CREDENTIALS'])
    # client = documentai.DocumentProcessorServiceClient(client_options=opts)
    cred = service_account.Credentials.from_service_account_info(
        st.secrets['GOOGLE_APPLICATION_CREDENTIALS']
    )
    client = documentai.DocumentProcessorServiceClient(credentials=cred)
    parent = client.common_location_path(project_id, "us")
    processor = client.create_processor(
        parent=parent,
        processor=documentai.Processor(
            type_="OCR_PROCESSOR",
            display_name=processor_display_name,
        ),
    )

    print(f"Processor Name: {processor.name}")

    if uploaded_file is not None:
        content = uploaded_file.read()

    raw_document = documentai.RawDocument(
        content=content,
        mime_type="image/jpeg",
    )
    request = documentai.ProcessRequest(name=processor.name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    print("The document contains the following text:")
    print(document.text)

process_label_button = st.button("Process Label", disabled=(uploaded_file is None))

# If the button is clicked and a file is uploaded, call the quickstart function
if process_label_button and uploaded_file is not None:
    quickstart(project_id, processor_display_name)

# Show a message when no file is uploaded
if uploaded_file is None:
    st.warning("Please upload a file to enable the 'Process Label' button.")