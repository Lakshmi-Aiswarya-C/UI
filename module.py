import streamlit as st

# Custom CSS to style the buttons
st.markdown("""
    <style>
        .container {
            display: flex;
            flex-direction: column; /* Arrange buttons vertically */
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 50px;
        }
        
        .button {
            background-color: #ffffff; /* Blue background */
            color: white; /* White text */
            padding: 15px 25px;
            font-size: 18px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, background-color 0.2s;
        }
        
        .button:hover {
            background-color: #0056b3; /* Darker blue on hover */
            transform: scale(1.1); /* Slightly enlarge on hover */
        }
        
        .button:active {
            transform: scale(1); /* Reset size on click */
        }
    </style>
""", unsafe_allow_html=True)

# Creating the buttons
st.markdown("""
    <div class="container">
        <a href="https://chatbot-medico.streamlit.app/" class="button">Module 1</a>
        <a href="https://tabletinfo.streamlit.app/" class="button">Module 2</a>
        <a href="https://medicalreportsummarizer.streamlit.app/" class="button">Module 3</a>
        <a href="http://127.0.0.1:5000/module4" class="button">Module 4</a>
        <a href="http://127.0.0.1:5000/module5" class="button">Module 5</a>
    </div>
""", unsafe_allow_html=True)
