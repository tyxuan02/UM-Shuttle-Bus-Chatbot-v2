import os
import re
import streamlit as st
import time
from jamaibase import JamAI
from PIL import Image
from dotenv import load_dotenv
from utils import get_table, create_action_table, create_knowledge_table, generate_response

# Load environment variables
load_dotenv()
JAMAI_BASE_PROJECT_ID = os.getenv("JAMAI_BASE_PROJECT_ID")
JAMAI_BASE_API_KEY= os.getenv("JAMAI_BASE_API_KEY")
ACTION_TABLE_ID = 'um-shuttle-bus-chatbot-action'
KNOWLEDGE_TABLE_ID = 'um-shuttle-bus-chatbot-knowledge'

st.set_page_config(page_title="UM Shuttle Bus Chatbot", page_icon="🚌")

# Initialize JamAI client
@st.cache_resource()
def initialize_client():
    """Initialize and cache the JamAI client."""
    return JamAI(token=JAMAI_BASE_API_KEY, project_id=JAMAI_BASE_PROJECT_ID)

# Initialize tables
@st.cache_data()
def initialize_tables(action_table_id, knowledge_table_id):
    """
    Check and create necessary tables for Jamaibase.

    Args:
        action_table_id (str): ID for the action table.
        knowledge_table_id (str): ID for the knowledge table.

    Returns:
        str: Status message indicating success or error.
    """
    try:
        # Check and create knowledge table if needed
        if not get_table("knowledge", knowledge_table_id):
            created_knowledge = create_knowledge_table()
            if not created_knowledge:
                return False
            
        # Check and create action table if needed
        if not get_table("action", action_table_id):
            created_action = create_action_table(action_table_id)
            if not created_action:
                return False

        return True
    except Exception as e:
        return f"Error during table initialization: {str(e)}"
    
# Stream response
def stream_response(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Initialize client and tables for Jamaibase
client = initialize_client()
status = initialize_tables(ACTION_TABLE_ID, KNOWLEDGE_TABLE_ID)

# Stop the app if there was an error initializing the tables
if status is False:
    st.error(f"Error initializing tables: Please make sure your API keys and project ID are correct.")
    st.stop()

st.title("🤖 UM Shuttle Bus Chatbot")
st.write("-----------\n\n")

# Reset chat
if st.sidebar.button("Reset chat"):
    st.session_state.pop("messages", None)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?", "images": []}]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "images" in message and len(message["images"]) > 0:
            for img_path in message["images"]:
                try:
                    image = Image.open(img_path)
                    st.image(image, use_container_width=True, caption=img_path.split("/")[-1])
                except Exception as e:
                    st.write(f"Error loading {img_path}: {e}")

# Handle new user input
if prompt := st.chat_input("Ask me something...", max_chars=500):
    # Display the user query
    with st.chat_message("user"):
        st.markdown(prompt)

    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt, "images": []})

    # Generate response
    response = generate_response(client, prompt)

    # Extract tags from the response
    tag_pattern = r'\[(.*?)\]$'
    match = re.search(tag_pattern, response)
    response_text = re.sub(tag_pattern, "", response).strip()  # Remove tags from the response

    tags = []
    if match:
        tags = match.group(1).split(", ")  # Extract and split the tags

    # Determine the images to display
    image_paths = []
    for tag in tags:
        if tag == "ROUTES":
            image_paths.append("images/ROUTES.png")
        elif tag == "SCHEDULE":
            image_paths.append("images/SCHEDULE_ALL_ROUTES.png")
        elif tag.startswith("ROUTE_"):
            image_paths.append(f"images/{tag}.png")
        elif tag.startswith("SCHEDULE_"):
            image_paths.append(f"images/{tag}.png")

   # Update the assistant message after generating the response
    with st.chat_message("assistant"):
        st.markdown(response_text)
        if len(image_paths) > 0:
            for img_path in image_paths:
                try:
                    image = Image.open(img_path)
                    st.image(image, use_container_width=True, caption=img_path.split("/")[-1])
                except Exception as e:
                    st.write(f"Error loading {img_path}: {e}")
                    
    # Append the assistant's response and images to session state
    st.session_state.messages.append({"role": "assistant", "content": response_text, "images": image_paths})