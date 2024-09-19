import streamlit as st
from scrape import scrape_website_with_scaperapi, split_dom_content, extract_body_content, clean_body_content
from parse import parse_with_ollama
from dotenv import load_dotenv
load_dotenv()
import os

st.title("AI Web Scrapper")
st.header("Effortless AI-Powered Web Scraping Tool")
url = st.text_input("Enter a website URL: ")
api_key = os.getenv('API_KEY')

if st.button("Scrape Site"):
    st.write('<p class="custom-text">Scrapping the website</p>', unsafe_allow_html=True)
    result = scrape_website_with_scaperapi(api_key, url)
    print(result)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    #save content
    st.session_state.dom_content = cleaned_content
    st.session_state.expander_open = True

if "dom_content" in st.session_state:
    if "expander_open" not in st.session_state:
        st.session_state.expander_open = False  
    
    with st.expander("View DOM content", expanded=st.session_state.expander_open):
        st.text_area("Dom Content", st.session_state.dom_content, height=300)
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            st.session_state.expander_open = True

            #pass to llm
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)


st.markdown("""
    <style>
    .stButton > button {
        background-color: #4ac7bc;
        color: #e4e4e4;
        padding: 10px 20px;
        font-size: 17px;
        border-radius: 8px;
        border: none;
    }
    
    .stButton > button:hover {
        background-color: #2d8078;
        color: #e4e4e4;
    }
            
    /* Title styling */
    h1 {
        color: #4ac7bc;
        font-size: 46px;
        font-weight: bold;
    }
    
    h2 {
        color: #4ac7bc;
        font-size: 28px;
        font-weight: bold;
    }
    
    input[type="text"] {
        background-color: #f0f0f0; 
        color: #010101;  
        padding: 10px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
    }
            
    input[type="text"]:focus, input[type="text"]:disabled {
        background-color: #f0f0f0 !important;
        color: #010101 !important; 
    }
    
    .streamlit-expanderHeader {
        font-size: 20px;
        color: #4CAF50;
        background-color: #f0f0f0;
        padding: 8px;
        border-radius: 5px;
    }

    .stTextArea textarea {
        background-color: #f0f0f0 !important;
        color: #010101 !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    </style>
    """, unsafe_allow_html=True)
