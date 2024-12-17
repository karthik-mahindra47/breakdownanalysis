import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate breakdown analysis
def generate_breakdown_analysis(breakdown_name):
    prompt = f"""
    You are an AI breakdown analyst for plant operations. 
    A breakdown is reported with the name: '{breakdown_name}'.

    Generate:
    1. Immediate Cause Analysis (ICA)
    2. Permanent Cause Analysis (PCA)
    3. Possible reasons
    4. Remedies to prevent this breakdown in the future.

    Format:
    ICA: [Immediate Cause]
    PCA: [Permanent Cause]
    Reasons: [Reasons in bullet points]
    Remedies: [Remedies in bullet points]
    """
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Plant Breakdown Analysis AI Tool")
st.write("Enter the breakdown name to generate ICA, PCA, possible reasons, and remedies.")

# User input
breakdown_name = st.text_input("Breakdown Name")

if st.button("Analyze Breakdown"):
    if breakdown_name:
        with st.spinner("Generating analysis..."):
            analysis = generate_breakdown_analysis(breakdown_name)
            st.subheader(f"Analysis for '{breakdown_name}':")
            st.text(analysis)
    else:
        st.warning("Please enter a breakdown name.")
