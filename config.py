import streamlit as st

class Config:
    openai_api_key = st.secrets["openai_api_key"]
    supabase_url = st.secrets["supabase_url"]
    supabase_key = st.secrets["supabase_key"]