import streamlit as st

st.set_page_config(page_title="UM Shuttle Bus Chatbot", page_icon="🚌")

# Title
st.title("📝 Disclaimer")
st.write("-----------\n\n")

with st.container():
    st.markdown("""
    <style>
    .container {
        padding: 2rem;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .content {
        font-size: 1.25rem;
        color: #555;
    }
    .highlight {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="container">
        <p class="content">
            The <span class="highlight">UM Shuttle Bus Chatbot</span> is designed to provide users with information about the UM Shuttle Bus service.
        </p>
        <p class="content">
            There may be scenarios where the chatbot provides a response that is not accurate or relevant to the user's query. This is due to limited data availability and the generative nature of the chatbot's responses.
        </p>
        <p class="content">
            For the most accurate and up-to-date information, please refer to the official UM Shuttle Bus service resources or contact the UM Shuttle Bus service directly.
        </p>
        <p class="content">
            Thank you for using the <span class="highlight">UM Shuttle Bus Chatbot</span>! 🚌
        </p>
    </div>
    """, unsafe_allow_html=True)