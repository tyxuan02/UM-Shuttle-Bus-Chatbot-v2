import streamlit as st

st.set_page_config(page_title="UM Shuttle Bus Chatbot", page_icon="🚌")

# Title
st.title("📖 UM Shuttle Bus Chatbot Guide")
st.write("-----------\n\n")

# Introduction
st.markdown("""
Welcome to the UM Shuttle Bus Chatbot! This chatbot is designed to provide information about the UM Shuttle Bus service. Here are some examples of the types of questions you can ask:
""")

# Sections with questions
st.subheader("Bus Routes")
st.markdown("""
- Please show me the bus routes available.
- Show me the bus stops for route AB.
- Is there route information for bus route C?
""")

st.subheader("Bus Schedule and Frequency")
st.markdown("""
- Can you show me the schedule for bus AB?
- How often do the buses run?
- How long does the shuttle bus take to travel from one stop to another?
""")

st.subheader("General Information")
st.markdown("""
- Do I need to have a UM student card to take the shuttle bus?
- Who should I contact if I left something on a shuttle bus?
- Are there any specific guidelines for using the shuttle bus service?
- Can I reserve the shuttle bus for a special event?
""")

# Limitations
st.write("\n\n")
st.markdown("""
**Limitation**: The chatbot does not provide real-time tracking of the shuttle buses. Besides, the chatbot cannot suggest direct routes to a specific bus stop or location.
""")

# Reminder
st.write("\n\n")
st.markdown("""
**Remember**: There may be scenarios where the chatbot provides a response that is not accurate or relevant to the user's query. This is due to limited data availability and the generative nature of the chatbot's responses. If you have a question that the chatbot can't answer, or if you need more detailed information, please check the official UM Shuttle Bus service resources. Besides, please ensure the words you use are correct and clear to get the best response from the chatbot.
""")