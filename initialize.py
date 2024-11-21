import requests
from dotenv import load_dotenv
import os

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
JAM_AI_BASE_API_KEY= os.getenv("JAM_AI_BASE_API_KEY")=

# Get table
def get_table(table_type, table_id):
    url = f'https://api.jamaibase.com/api/v1/gen_tables/{table_type}/{table_id}'

    try:
        response = requests.get(url, headers={
            'X-PROJECT-ID': PROJECT_ID,
            'Authorization': f'Bearer {JAM_AI_BASE_API_KEY}',
            'Content-Type': 'application/json'
        })
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Validate the response structure
            table_id = data.get('id')
            if table_id is not None:
                return table_id == str(table_id)
            else:
                print("Key 'id' not found in the response.")
                return False
        elif response.status_code == 404:
            print("Key 'id' not found in the response.")
            return False
        else:    
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        # Handle network or other connection errors
        print(f"Exception occurred: {e}")
        return False
    
def create_action_table(table_id):
    url = f'https://api.jamaibase.com/api/v1/gen_tables/action'

    try:
        response = requests.post(url, headers={
            'X-PROJECT-ID': PROJECT_ID,
            'Authorization': f'Bearer {JAM_AI_BASE_API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }, 
        json={
            'id': str(table_id),
            'cols': [
                {
                    'id': 'query',
                    "dtype": "str"
                },
                {
                    "id": "response",
                    "dtype": "str",
                    "gen_config": {
                        "object": "gen_config.llm",
                        "max_tokens": 100
                    }
                },
                {
                    "id": "img",
                    "dtype": "str",
                    "gen_config": {
                        "object": "gen_config.llm",
                        "system_prompt": "Respond only if the query matches a tag in the knowledge table, else do not respond.",
                    }
                }
            ],
        })
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Action table created successfully")
            return True
        else:
            print(response.json())
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        # Handle network or other connection errors
        print(f"Exception occurred: {e}")
        return False
    
def create_knowledge_table(table_id):
    url = f'https://api.jamaibase.com/api/v1/gen_tables/knowledge'

    try:
        response = requests.post(url, headers={
            'X-PROJECT-ID': PROJECT_ID,
            'Authorization': f'Bearer {JAM_AI_BASE_API_KEY}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }, 
        json={
            'id': str(table_id),
            'cols': [
                {
                    'id': 'tag',
                    "dtype": "str"
                },
                {
                    "id": "response",
                    "dtype": "str",
                    "gen_config": {
                        "object": "gen_config.llm",
                        "max_tokens": 100
                    }
                },
                {
                    "id": "img",
                    "dtype": "str",
                    "gen_config": {
                        "object": "gen_config.llm",
                        "system_prompt": "Respond only if the query matches a tag in the knowledge table, else do not respond.",
                    }
                }
            ],
        })
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Knowledge table created successfully")
            return True
        else:
            print(response.json())
            print(f"Error: Received status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        # Handle network or other connection errors
        print(f"Exception occurred: {e}")
        return False
    
def create_knowledge_table():
    url = f'https://api.jamaibase.com/api/v1/gen_tables/knowledge/import'

    try:
        response = requests.post(url, headers={
            'X-PROJECT-ID': PROJECT_ID,
            'Authorization': f'Bearer {JAM_AI_BASE_API_KEY}',
            'Accept': 'application/json',
        },
        files={
            'file': ('1.parquet', open('1.parquet', 'rb'), 'application/octet-stream')
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
    
from jamaibase import JamAI, protocol as p

jamai = JamAI(token=JAM_AI_BASE_API_KEY, project_id=PROJECT_ID)

def test(query):
    try:
        completion = jamai.table.add_table_rows(
            "action",
            p.RowAddRequest(
                table_id="123",
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

# # result = get_table("chat",1234567890)
# # print(result)

# # result = create_action_table("h1aha")
# # print(result)

# result = create_knowledge_table()
# print(result)

# result = test("show me the route for bus 13")
# print(result)


