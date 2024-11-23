import requests
import os
import requests
from jamaibase import JamAI, protocol as p
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
JAMAI_BASE_PROJECT_ID = os.getenv("JAMAI_BASE_PROJECT_ID")
JAMAI_BASE_API_KEY = os.getenv("JAMAI_BASE_API_KEY")

# Get table
def get_table(table_type, table_id):
    url = f'https://api.jamaibase.com/api/v1/gen_tables/{table_type}/{table_id}'
    try:
        response = requests.get(url, headers={
            'X-PROJECT-ID': JAMAI_BASE_PROJECT_ID,
            'Authorization': f'Bearer {JAMAI_BASE_API_KEY}',
            'Content-Type': 'application/json',
        })
        if response.status_code == 200:
            data = response.json()
            return data.get('id') == str(table_id)
        elif response.status_code == 404:
            print("Table not found.")
            return False
        else:
            print(f"Error: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Exception occurred: {e}")
        return False

# Create action table
def create_action_table(table_id):
    url = f'https://api.jamaibase.com/api/v1/gen_tables/action'
    try:
        response = requests.post(url, headers={
            'X-PROJECT-ID': JAMAI_BASE_PROJECT_ID,
            'Authorization': f'Bearer {JAMAI_BASE_API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }, json={
            'id': str(table_id),
            'cols': [
                {'id': 'query', 'dtype': 'str'},
                {
                    "id": "response",
                    "gen_config": {
                        "object": "gen_config.llm",
                        "model": "ellm/meta-llama/Llama-3.1-70B-Instruct",
                        "system_prompt": "You are a versatile data generator responsible for processing input data and generating appropriate responses based on the specified column name and query. Tailor your response format and content according to the column name and context of the query, ensuring the answers are concise, relevant, and efficient without including unnecessary details or lengthy lists. Analyze the content for any metadata tags (e.g., [ROUTE], [SCHEDULE], etc.) to determine the context of the query. If a tag is detected (only the tag in the knowledge table), include it at the end of the response to indicate the relevant context (multiple tags allowed if applicable and store them in array format). Only return the tag if the questions are related to the route or schedule.",
                        "prompt": "Table name: \"test\" query: ${query}. Based on the available information, provide an appropriate response for the column \"response\". Remember to act as a cell in a spreadsheet and provide concise, relevant information with an explanation if needed.",
                        "rag_params": {
                            "table_id": "um-shuttle-bus-chatbot-knowledge",
                            "k": 5
                        },
                        "top_p": 0.001,
                        "max_tokens": 2000
                    },
                    "dtype": "str"
                },
            ],
        })
        # Check if the request was successful
        if response.status_code == 200:
            print("Action table created successfully")
            return True
        else:
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Exception occurred: {e}")
        return False

# Create knowledge table
def create_knowledge_table():
    url = f'https://api.jamaibase.com/api/v1/gen_tables/knowledge/import'

    try:
        response = requests.post(url, headers={
            'X-PROJECT-ID': JAMAI_BASE_PROJECT_ID,
            'Authorization': f'Bearer {JAMAI_BASE_API_KEY}',
            'Accept': 'application/json',
        },
        files={
            'file': ('um-shuttle-bus-chatbot-knowledge.parquet', open('um-shuttle-bus-chatbot-knowledge.parquet', 'rb'), 'application/octet-stream')
        })
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Knowledge table created successfully")
            return True
        else:
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        # Handle network or other connection errors
        print(f"Exception occurred: {e}")
        return False
    
def generate_response(client, query):
    try:
        completion = client.table.add_table_rows(
            "action",
            p.RowAddRequest(
                table_id="um-shuttle-bus-chatbot-action",
                data=[{"query": query}],
                stream=False,
            ),
        )
        if completion.rows[0]:
            return completion.rows[0].columns["response"].text
        else:
            return "No response"
    except Exception as e:
        return str(e)