# Basic type imports
from typing import List, Dict, Union
import logging

logger = logging.getLogger("goodfoods")
logger.info("Tool schema loaded")

restaurant_tools: List[Dict[str, Union[str, Dict]]] = [

    # ---------------------------------------------------
    # 1️⃣ Restaurant Search Tool (SIMPLIFIED)
    # ---------------------------------------------------
    {
        "type": "function",
        "function": {
            "name": "lookup_dining_options",
            "description": "Search for restaurants using user-provided filters like location or cuisine.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Restaurant name if user specifies."
                    },
                    "location": {
                        "type": "string",
                        "description": "Area or landmark mentioned by user."
                    },
                    "cuisine": {
                        "type": "string",
                        "description": "Cuisine type mentioned by user."
                    },
                    "operating_days": {
                        "type": "string",
                        "description": "Day of the week if specified."
                    },
                    "operating_time": {
                        "type": "string",
                        "description": "Time preference in HH:MM format."
                    }
                }
            }
        }
    },

    # ---------------------------------------------------
    # 2️⃣ Reservation Confirmation Tool
    # ---------------------------------------------------
    {
        "type": "function",
        "function": {
            "name": "confirm_table_booking",
            "description": "Confirm a restaurant reservation after collecting all required details.",
            "parameters": {
                "type": "object",
                "required": [
                    "restaurant_id",
                    "orderer_name",
                    "orderer_contact",
                    "party_size",
                    "reservation_date",
                    "reservation_time"
                ],
                "properties": {
                    "restaurant_id": {
                        "type": "string",
                        "description": "Restaurant ID from search results."
                    },
                    "orderer_name": {
                        "type": "string",
                        "description": "Customer's name."
                    },
                    "orderer_contact": {
                        "type": "string",
                        "description": "Customer phone number."
                    },
                    "party_size": {
                        "type": "integer",
                        "description": "Number of guests."
                    },
                    "reservation_date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format."
                    },
                    "reservation_time": {
                        "type": "string",
                        "description": "Time in HH:MM format."
                    }
                }
            }
        }
    }
]