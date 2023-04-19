import streamlit as st
import GPT_PDF_II as gpt_II

st.set_page_config(page_title='PDF Query GPT Bot',page_icon=':tada:',layout='wide')

st.title('This is a PDF Query Bot based on ChatGPT!!!')

pdf_path = st.text_input('Input the pdf path here :')

query = st.text_input('Input your query here :')

button = st.button("Run Query!")

if button:
    OpenAI_API_Key = "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" 
    gpt = gpt_II.GPT_PDF(pdf_path,OpenAI_API_Key)
    result = gpt.query_corp(query)
    st.write(f'### Results: {result}')
