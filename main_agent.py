import os
import openai
import sys
from tools import HeartDiseaseDBTool, CancerDBTool, DiabetesDBTool, MedicalWebSearchTool
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL") 
API_KEY = os.getenv("API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME") 

# Initialize OpenAI async client
if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set BASE_URL, API_KEY, and MODEL_NAME."
    )
    

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

# Set up your OpenAI API key
# openai.api_key = "YOUR_API_KEY"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main_agent.py \"<your_question>\"")
        sys.exit(1)

    user_question = sys.argv[1]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "HeartDiseaseDBTool",
                "description": "Queries the heart disease database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The SQL query to execute."
                        }
                    },
                    "required": ["query"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "CancerDBTool",
                "description": "Queries the cancer database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The SQL query to execute."
                        }
                    },
                    "required": ["query"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "DiabetesDBTool",
                "description": "Queries the diabetes database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The SQL query to execute."
                        }
                    },
                    "required": ["query"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "MedicalWebSearchTool",
                "description": "Searches the web for medical information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query."
                        }
                    },
                    "required": ["query"]
                }
            }
        }
    ]

    messages = [
        {"role": "system", "content": "You are a helpful medical assistant. Route the user's question to the appropriate tool."},
        {"role": "user", "content": user_question}
    ]

    response = openai.OpenAIChatCompletionsModel.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    response_message = response.choices[0].message

    if response_message.tool_calls:
        available_functions = {
            "HeartDiseaseDBTool": HeartDiseaseDBTool,
            "CancerDBTool": CancerDBTool,
            "DiabetesDBTool": DiabetesDBTool,
            "MedicalWebSearchTool": MedicalWebSearchTool,
        }
        function_name = response_message.tool_calls[0].function.name
        function_to_call = available_functions[function_name]
        function_args = response_message.tool_calls[0].function.arguments
        function_response = function_to_call(**eval(function_args))
        print(function_response)
    else:
        print(response_message.content)

if __name__ == "__main__":
    main()
