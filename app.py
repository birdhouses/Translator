# app.py

import streamlit as st
from modules.translator import Translator
import os
import pandas as pd

def main():
    st.title("Robust Translator Application")

    assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
    translator = Translator(assistant_id)

    uploaded_file = st.file_uploader(
        "Upload a CSV or Text File", type=["csv", "txt", "md"]
    )
    source_language = st.selectbox(
        "Select Source Language",
        options=[
            "Detect Language",
            "English",
            "Spanish",
            "French",
            "German",
            "Chinese",
            "Japanese",
            "Korean",
        ],
    )
    target_language = st.selectbox(
        "Select Target Language",
        options=[
            "English",
            "Spanish",
            "French",
            "German",
            "Chinese",
            "Japanese",
            "Korean",
        ],
    )
    model_name = st.text_input("Model Name", value="gpt-4o-mini")

    if st.button("Translate") and uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        if file_extension == '.csv':
            df = pd.read_csv(uploaded_file)
            text = df.to_csv(index=False)
        else:
            text = uploaded_file.read().decode('utf-8')

        # Initialize the progress bar and status text
        progress_bar = st.progress(0)
        status_text = st.empty()

        def progress_callback(progress):
            progress_bar.progress(progress)
            status_text.text(f"Translation progress: {int(progress * 100)}%")

        with st.spinner("Translating..."):
            translated_text = translator.translate_text(
                text,
                source_language,
                target_language,
                model_name,
                progress_callback=progress_callback,
            )
        st.success("Translation completed!")

        # Clear the progress bar and status text
        progress_bar.empty()
        status_text.empty()

        st.download_button(
            "Download Translated Text",
            data=translated_text,
            file_name=f"translated_{uploaded_file.name}",
        )
        st.text_area("Translated Text", translated_text, height=300)

if __name__ == '__main__':
    main()
