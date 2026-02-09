import streamlit as st
import requests 

st.set_page_config(page_title = 'Enterprise Document Search', layout = 'wide')

st.title('Enterprise Document Search')
st.write('Ask questions about corporate and legal policies')

question = st.text_input("Your question here: ")
col1, col2 = st.columns([1, 1])

with col1:
    ask_btn = st.button('Ask')

with col2:
    clear_btn = st.button('Clear')

if clear_btn:
    st.rerun()

if ask_btn and question: 
    with st.spinner("Searching Document and generating text..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json = {
                    "question": question,
                    "k": 10
                },
                timeout = 120
            )

            data = response.json()

            st.subheader("Answer")
            st.success(data['answer'])

            if data['grounded']:
                st.info("Grounded in retrieved document")
            else:
                st.warning("Answer may not be fully grounded.")

            st.header("Sources")

            for src in data["sources"]:
                st.write(
                    f" - **{src['doc_name']}** "
                    f"(Page {src['page']}) "
                    f"[{src['domain']}]"
                )

        except Exception as e:
            st.error("Could not connect to backend. Is FastAPI running?")
            st.text(str(e))