import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load lottie animation
def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Lottie Animation
lottie_hero = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x62chJ.json")

# Page Config
st.set_page_config(page_title="CARE AI – Intelligent Medical Chatbot", page_icon="💡", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to bottom right, #121212, #343434);
            color: #ffffff;
        }
        .hero, .about, .contact, .footer {
            padding: 30px;
            text-align: center;
        }
        .button {
            padding: 12px 24px;
            font-size: 1.1em;
            background-color: #1a73e8;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background-color 0.3s ease;
            display: inline-block;
        }
        .button:hover {
            background-color: #1558b0;
        }
        ul {
            text-align: left;
            max-width: 800px;
            margin: 0 auto;
        }
        .footer {
            font-size: 0.9em;
            color: #bbbbbb;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
selected = st.sidebar.selectbox("Go to", [
    "Home",
    "About",
    "Methodology",
    "Chatbot",
    "Tablet Info Summarizer",
    "Lab Report Analyzer",
    "Diet Plan Suggestor",
    "Contact"
])

# --- Home ---
if selected == "Home":
    st.markdown("""
    <div class="hero">
        <h1 style="font-size: 2.5em;">CARE AI – Intelligent Medical Chat Assistant</h1>
        <p style="font-size: 1.3em;">Bringing clarity and support to your everyday health questions through AI-powered dialogue.</p>
        <p style="font-size: 1.1em;">Our mission is to simplify medical information access and improve health literacy for everyone.</p>
    </div>
    """, unsafe_allow_html=True)

    if lottie_hero:
        st_lottie(lottie_hero, height=300, key="hero_animation")

    st.markdown("""
    <div style="text-align: center; padding-top: 20px;">
        <a href="http://localhost:8501/" class="button" target="_blank">Launch Chat Assistant</a>
    </div>
    """, unsafe_allow_html=True)

# --- About ---
elif selected == "About":
    st.markdown("""
    <div class="about">
        <h2>About CARE AI</h2>
        <p style="font-size: 1.1em;">
            CARE AI is a unified conversational platform designed to simplify the way individuals interact with health information.
            By leveraging advanced AI and LLM technologies, it guides users in understanding medical reports, medications, and diet plans.
        </p>
    </div>

    <div class="about">
        <h2>System Capabilities</h2>
        <ul style="font-size: 1.1em; line-height: 1.8;">
            <li><strong>Disease Information:</strong> Insights into symptoms, causes, and treatments.</li>
            <li><strong>Tablet Info Summarizer:</strong> Upload a tablet image and get clear details about usage and effects.</li>
            <li><strong>Lab Report Analyzer:</strong> Summarizes lab results using AI, with layman explanations.</li>
            <li><strong>Diet Plan Suggestor:</strong> Personalized meal planning using user data and AI models.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Methodology ---
elif selected == "Methodology":
    st.title("Development Methodology")
    st.markdown("""
    <p style="font-size: 1.1em;">
        CARE AI uses a modular approach that combines conversational AI with domain-specific processing for lab reports, diet plans, and medications.
    </p>
    <ul style="font-size: 1.1em; line-height: 1.8;">
        <li><strong>Intent Detection:</strong> The chatbot determines the user’s query type (e.g., diet, lab, medicine).</li>
        <li><strong>Lab Report Summarizer:</strong> Extracts and simplifies insights using AI-powered image and text parsing.</li>
        <li><strong>Tablet Info Summarizer:</strong> Uses OCR/NLP to fetch dosage, side effects, usage information.</li>
        <li><strong>Diet Planner:</strong> Uses user profile and KNN to match meal options with calorie and health needs.</li>
    </ul>
    """, unsafe_allow_html=True)

# --- Chatbot ---
elif selected == "Chatbot":
    st.title("Medical Chatbot")
    st.markdown("""
        <p>Ask general medical queries or get assistance with reports, tablets, or diet plans.</p>
        <a href="http://localhost:8501/" class="button" target="_blank">Open Chat Assistant</a>
    """, unsafe_allow_html=True)

# --- Tablet Info Summarizer ---
elif selected == "Tablet Info Summarizer":
    st.title("Tablet Info Summarizer")
    st.write("Upload a medicine image or use the tool below:")
    st.markdown("""
        <a href="https://5df9nqf5y2dqv2w7ev6xza.streamlit.app/" class="button" target="_blank">
            Open Tablet Info Summarizer
        </a>
    """, unsafe_allow_html=True)

# --- Lab Report Analyzer ---
elif selected == "Lab Report Analyzer":
    st.title("Lab Report Analyzer")
    st.write("Upload your diagnostic report or visit the analysis tool:")
    st.markdown("""
        <a href="https://fxvmph62r948bafhhj8meh.streamlit.app/" class="button" target="_blank">
            Open Lab Report Analyzer
        </a>
    """, unsafe_allow_html=True)

# --- Diet Plan Suggestor ---
elif selected == "Diet Plan Suggestor":
    st.title("Diet Plan Suggestor")
    st.write("Enter your health information or use the dedicated planner:")
    st.markdown("""
        <a href="https://8z3sw876xnebjntbj26r8b.streamlit.app/" class="button" target="_blank">
            Open Diet Plan Suggestor
        </a>
    """, unsafe_allow_html=True)

# --- Contact ---
elif selected == "Contact":
    st.markdown("""
    <div class="contact">
        <h2>Contact Us</h2>
        <p style="font-size: 1.1em;">For questions or feedback, please reach out to our team.</p>
        <p style="font-size: 1.1em;"><strong>Email:</strong> careai.support@gmail.com</p>
        <p style="font-size: 1.1em;"><strong>Location:</strong> Thiruparankundram, Tamil Nadu – 625015</p>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>&copy; 2025 CARE AI. Final Year Project – Dept. of IT, KLNCE</p>
</div>
""", unsafe_allow_html=True)
