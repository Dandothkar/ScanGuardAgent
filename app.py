from utils import init_env
import streamlit as st
import pandas as pd
from pipeline.wrapper import classify_message, classify_batch
from pydantic import ValidationError

init_env()

### STREAMLIT APPLICATION BEGINS
## Overall headings
st.set_page_config(page_title="Spam Detector", page_icon="📧")
st.title("📧 Spam Detector (Gemini + LangChain)")

# Creating two tabs, one for single message, one for batch upload
tab1, tab2 = st.tabs(["Single Message", "Batch CSV upload"])

# Single message tab begins
with tab1:
    st.subheader("Paste an email or message and detect if it's **Spam / Not Spam / Uncertain**.")
    user_input = st.text_area("Message to classify:", height=150)

    if st.button("Classify"):
        if not user_input.strip():
            st.warning("Please enter a message.")
        else:
            try:
                result = classify_message(user_input)
    
                st.subheader("Classification Result")
                st.write("**Label:**", result.label)
                st.write("**Risk Score:**", result.risk_score)
                st.write("**Reasons:**", result.reasons)
                st.write("**Red Flags:**", result.red_flags)
                st.write("**Suggested Action:**", result.suggested_action)
    
                with st.expander("Raw JSON"):
                    st.json(result.model_dump())
    
            except ValidationError as e:
                st.error(f"Validation failed: {e}")

# Batch upload tab begins
with tab2:
    st.subheader("Upload a csv file")
    # Upload the csv
    uploaded =st.file_uploader("Upload a csv from the directory", type = "csv")
    # Read csv on uploading
    if(uploaded):
        df = pd.read_csv(uploaded)
        # CHeck if the data read is empty
        if(not df.columns.tolist()):
            st.error("Upload a csv with proper information")
        else:
            # If button is clicked
            if(st.button("Run Batch Classification", key = 'batch')):
                # Get first column of Dataframe as list
                results_df = classify_batch(df.iloc[:,0].tolist())
                st.dataframe(results_df, use_container_width = True)