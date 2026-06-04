# app.py

import streamlit as st
import pandas as pd
from utils.checks import *
from agents.quality_agent import generate_insights

st.set_page_config(page_title="AI Data Quality Agent")

st.title("🤖 AI Data Quality Agent")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Data Quality Score")

    score = get_quality_score(df)

    st.metric("Quality Score", f"{score}/100")
    st.subheader("Missing Values Analysis")

    missing = get_missing_values(df)

    missing_df = missing[missing > 0]

    if len(missing_df) > 0:
        st.dataframe(missing_df)
    else:
        st.success("No missing values found.")

    st.subheader("Duplicate Records")

    duplicates = get_duplicate_count(df)

    st.metric("Duplicate Rows", duplicates)

    if duplicates > 0:
        st.warning("Duplicate records detected.")
    else:
        st.success("No duplicate records found.")
    
    st.subheader("AI Agent Findings")

    findings = generate_insights(df)

    for item in findings:
        st.info(item)