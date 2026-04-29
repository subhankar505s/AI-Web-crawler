import streamlit as st 
from crawler import (
     scrape_website,
     split_dom_content,
     extract_body_content,
     clean_body_content )
from parse import parse_with_ollama

st.title("Spindle AI Web Crawler")
url=st.text_input("Enter a website URL: ")

if st.button("Crawl site"):
    st.write("crawling the website")

    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descrive what you want to parse from the website content? ")

    if st.button("parse Content"):
        if parse_description:
            st.write("Parsing the Content ...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)