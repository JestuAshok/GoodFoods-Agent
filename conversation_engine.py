# Basic Imports
import json
import re
import requests
import os
from typing import Union
from dotenv import load_dotenv

# Third-party Imports
from groq import Groq

# Load environment variables
load_dotenv()

# Internal Imports
from data.service_api import *

# Setup logging
import logging
logger = logging.getLogger("goodfoods")

# Global Constant
BASE_URL = "http://localhost:8000"
logger.info(f"BASE URL for API calls set as: {BASE_URL}")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def collect_user_console_message() -> dict[str, str]:
    user_input = input("USER>")
    return {"role": "user", "content": user_input}


def generate_chat_completion(
    api_key,
    conversation_history: list,
    tools: list,
    model_type="llama-3.1-8b-instant",
    tool_calling_enabled: bool = False,
):
    """
    Make API call to Groq model with conversation history.
    """

    try:
        # 🔥 IMPORTANT: Limit history to prevent token overflow
        conversation_history = conversation_history[-6:]

        if tool_calling_enabled:
            ai_api_response_obj = client.chat.completions.create(
                model=model_type,
                messages=conversation_history,
                tools=tools,
                tool_choice="auto",
            )
        else:
            ai_api_response_obj = client.chat.completions.create(
                model=model_type,
                messages=conversation_history,
            )

        return ai_api_response_obj

    except Exception as e:
        logger.error(f"Groq API call failed: {str(e)}", exc_info=True)
        raise


def normalize_chat_response(api_response_obj: object) -> Union[list, dict]:
    message = api_response_obj.choices[0].message

    # Tool calls present
    if hasattr(message, "tool_calls") and message.tool_calls:
        logger.info("The agent response includes tool calls.")
        return message.tool_calls

    # Normal assistant text
    if message.content:
        logger.info("The agent response includes message content.")
        return {"role": "assistant", "content": message.content}

    return {"role": "assistant", "content": ""}


def execute_tool_calls(list_of_tool_calls: list) -> list:
    list_of_tool_call_responses = []

    for tool_call in list_of_tool_calls:
        function_name = tool_call.function.name

        # Safer argument parsing
        try:
            function_args = json.loads(tool_call.function.arguments)
        except Exception:
            function_args = {}

        function_response = dispatch_backend_tool(function_name, function_args)

        if isinstance(function_response, (list, dict)):
            function_response = json.dumps(function_response)

        tool_call_response_formatted = {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": function_name,
            "content": function_response,
        }

        logger.info(tool_call_response_formatted)
        list_of_tool_call_responses.append(tool_call_response_formatted)

    return list_of_tool_call_responses


def dispatch_backend_tool(function_name: str, function_args: dict) -> Union[dict, str]:

    try:
        if function_name == "lookup_dining_options":
            response = requests.post(
                f"{BASE_URL}/restaurants/search",
                json=function_args,
            )
            return response.json()

        elif function_name == "confirm_table_booking":
            response = requests.post(
                f"{BASE_URL}/reservations",
                json=function_args,
            )
            return response.json()

        else:
            return {"error": f"No tool found with name {function_name}"}

    except Exception as e:
        logger.error(f"Backend tool error: {str(e)}", exc_info=True)
        return {"error": str(e)}


def has_function_simulation(response_text: str) -> bool:
    patterns = [
        r"<function[^>]*>",
        r"<tool[^>]*>",
        r"function\([^)]*\)",
        r"tool\([^)]*\)",
        r"confirm_table_booking\([^)]*\)",
        r"lookup_dining_options\([^)]*\)",
    ]

    for pattern in patterns:
        if re.search(pattern, response_text, re.IGNORECASE):
            return True

    return False