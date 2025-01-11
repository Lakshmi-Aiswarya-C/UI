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
st.set_page_config(page_title="CARE AI - AI Assistance for Medical", page_icon="✨", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to bottom right, #121212, #343434);
            color: #ffffff;
        }
        .header {
            text-align: center;
            padding: 10px 0;
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

# Header Section
st.markdown("""
<div class="header">
    <h1>🌟 CARE AI - AI Assistance for Medical 🌟</h1>
    <p>
        <a href="#home" style="color: #FFD700; margin-right: 20px;">Home</a>
        <a href="#about" style="color: #FFD700; margin-right: 20px;">About</a>
        <a href="#contact" style="color: #FFD700;">Contact</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Hero Section with Animation
st.markdown("""
<div class="hero">
    <h1 style="font-size: 2.5em;">AI Assistance for Medical</h1>
    <p style="font-size: 1.5em;">Bringing Medical Help at Your Fingertips</p>
</div>
""", unsafe_allow_html=True)

# Add Lottie Animation
if lottie_hero:
    st_lottie(lottie_hero, height=300, key="hero_animation")

# Modules Button
st.markdown("""
    <style>
        .hero {
            text-align: center;
            padding: 20px;
        }

        .button {
            background-color:#ffffff; /* Blue background */
            color: #000000; /* White text */
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            display: inline-block;
        }

        .button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Creating the button using HTML
st.markdown('<div class="hero"><a href="https://modules.streamlit.app/" class="button">Explore Modules</a></div>', unsafe_allow_html=True)


# About Us Section
st.markdown("""
<div class="about">
    <h2>About Us</h2>
    <p style="font-size: 1.2em;">
        CARE AI is designed to assist users with medical-related queries and tasks through advanced AI capabilities.
        With four key modules, our platform helps with disease information, tablet identification, medical report analysis,
        and personalized diet plans.
    </p>
</div>
""", unsafe_allow_html=True)

# Modules Description Section
st.markdown("""
<div class="about">
    <h2>Our Modules</h2>
    <ul style="font-size: 1.2em;">
        <li><b>Disease Query Chat Application:</b> Chat system answering user questions about diseases (symptoms, causes, treatment).</li>
        <li><b>Tablet Info Retrieval:</b> Identify tablets from images and provide usage, dosage, and side effect details.</li>
        <li><b>Medical Report Summarizer:</b> Extract and summarize key insights from uploaded medical reports.</li>
        <li><b>Diet Plan Suggestion:</b> Generate personalized diet plans based on user health data and preferences.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact">
    <h2>Contact Us</h2>
    <p style="font-size: 1.1em;"><b>Phone:</b> 9786347455</p>
    <p style="font-size: 1.1em;"><b>Email:</b> careai@gmail.com</p>
    <p style="font-size: 1.1em;"><b>Address:</b> Thiruparankundram, Tamil Nadu 625015</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Copyright © 2022 CARE AI. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
