import streamlit as st
from google.cloud import documentai
from google.oauth2 import service_account
import io
import google.generativeai as genai
from utility.gemini_function_calling_schema import get_product_profile

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

def _ocr_foodlabel(pdf_file):
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

def _get_product_profile(input_text: str):
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model1 = genai.GenerativeModel('gemini-pro')
    model2 = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest', tools=[get_product_profile])
    response1 = model1.generate_content(
        f'''
        Identify the name and brand of the product, the proprietary claims made in regards to it, the ingredients, the serving size and the nutritional information:
        {input_text}
        '''
    )
    result1 = response1.text
    print(result1)
    response = model2.generate_content(f"""
                    Please provide a detailed product profile based on the following input:
                    - Include the product name, proprietary claims, ingredients, serving size, and nutritional information (including values per 100g and % RDA for each item).
                    - The input text is:
                    {result1}
                    """,
                    tool_config={'function_calling_config': 'ANY'}
                )
    
    result2 = response.candidates[0].content.parts[0].function_call
    result = type(result2).to_dict(result2)
    print(type(result))
    print(result)
    return result

def _get_health_analysis(product_profile: str):
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest', tools = [get_financial_data])
    response = model.generate_content(f"""
                    Please add the yearwise financial metric values to the database:
                                       {product_profile}
                    """,
                    tool_config={'function_calling_config':'ANY'}
                )
    result = response.candidates[0].content.parts[0].function_call
    result = type(result).to_dict(result)
    print(type(result))
    return result

def health_analysis(packaged_food_label):
    food_label_text = _ocr_foodlabel(packaged_food_label)
    product_profile = _get_product_profile(food_label_text)
    # product_health_analysis = _get_health_analysis(product_profile)
    # return product_health_analysis