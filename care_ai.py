import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load lottie animations
def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Lottie Animation URL
lottie_hero = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x62chJ.json")

# Page Config
st.set_page_config(page_title="CARE AI - Intelligent Medical Chatbot", page_icon="💡", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to bottom right, #121212, #343434);
            color: #ffffff;
        }
        .hero {
            text-align: center;
            margin: 20px auto;
        }
        .button {
            padding: 10px 20px;
            font-size: 1.2em;
            background-color: #5A8DEE;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            border: none;
        }
        .about, .contact, .footer {
            padding: 40px 20px;
            margin-top: 30px;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #bbbbbb;
        }
    </style>
""", unsafe_allow_html=True)

# --- Navigation using radio buttons ---
selected = st.radio("Navigation", ["Home", "About", "Contact"], horizontal=True)

# --- Home Section ---
if selected == "Home":
    st.markdown("""
    <div class="hero">
        <h1 style="font-size: 2.5em;">🤖 CARE AI - Intelligent Medical Chatbot 🤖</h1>
        <p style="font-size: 1.5em;">Your One-Stop AI Health Assistant</p>
        <p style="font-size: 1.2em;">Ask your medical questions. Get instant, smart help.</p>
    </div>
    """, unsafe_allow_html=True)

    if lottie_hero:
        st_lottie(lottie_hero, height=300, key="hero_animation")

    st.markdown("""
    <div style="text-align: center; padding-top: 20px;">
        <a href="https://careai-chat.streamlit.app/" class="button">Start Chatbot</a>
    </div>
    """, unsafe_allow_html=True)

# --- About Section ---
elif selected == "About":
    st.markdown("""
    <div class="about">
        <h2>About CARE AI</h2>
        <p style="font-size: 1.2em;">
            CARE AI is an AI-powered chatbot platform designed to assist users in managing health-related concerns via an interactive chat experience.
            It integrates specialized modules for deeper assistance based on user needs.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about">
        <h2>Integrated Modules</h2>
        <ul style="font-size: 1.2em;">
            <li><b>🧠 Disease Chatbot:</b> Instantly answers queries about symptoms, causes, and treatments.</li>
            <li><b>💊 Tablet Info Summarizer:</b> Upload a medicine image to identify its purpose and effects.</li>
            <li><b>📑 Lab Report Analyzer:</b> Get health insights by uploading medical reports (PDF).</li>
            <li><b>🥗 Diet Plan Suggestor:</b> Personalized nutrition plans based on your condition and preferences.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Contact Section ---
elif selected == "Contact":
    st.markdown("""
    <div class="contact">
        <h2>Contact Us</h2>
        <p style="font-size: 1.1em;"><b>Email:</b> careai@gmail.com</p>
        <p style="font-size: 1.1em;"><b>Address:</b> Thiruparankundram, Tamil Nadu 625015</p>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>© 2025 CARE AI. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
