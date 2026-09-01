import os
import json

from dotenv import load_dotenv
from google import genai


from database_tools import (
    verify_customer,
    get_renewal_details,
    search_products,
    create_customer,
    save_interest
)


load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in .env"
    )

client = genai.Client(
    api_key=api_key
)


MODEL = "gemini-3.6-flash"

tools = [

    {
        "type": "function",
        "name": "verify_customer",
        "description": (
            "Verify whether a customer ID exists. "
            "Use this when the customer provides an ID "
            "or wants to verify existing customer status."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": (
                        "Customer ID such as CUST1001"
                    )
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "type": "function",
        "name": "get_renewal_details",
        "description": (
            "Get renewal information for an existing customer. "
            "Returns product name, expiry date and renewal amount."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID"
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "type": "function",
        "name": "search_products",
        "description": (
            "Search products by category. "
            "Use this when a customer asks about products "
            "or wants products based on an interest."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": (
                        "Category such as Grocery, Electronics, "
                        "Clothing, Appliances, Books, Sports or Toys"
                    )
                }
            },
            "required": ["category"]
        }
    },

    {
        "type": "function",
        "name": "create_customer",
        "description": (
            "Create a new customer after collecting "
            "their required personal information."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Customer full name"
                },
                "email": {
                    "type": "string",
                    "description": "Customer email address"
                },
                "phone": {
                    "type": "string",
                    "description": "Customer phone number"
                },
                "dob": {
                    "type": "string",
                    "description": "Customer date of birth"
                },
                "city": {
                    "type": "string",
                    "description": "Customer city"
                }
            },
            "required": [
                "name",
                "email",
                "phone"
            ]
        }
    },

    {
        "type": "function",
        "name": "save_interest",
        "description": (
            "Save a customer's product interest."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID"
                },
                "category": {
                    "type": "string",
                    "description": "Interested product category"
                }
            },
            "required": [
                "customer_id",
                "category"
            ]
        }
    }
]

def execute_tool(name, arguments):

    if name == "verify_customer":

        return verify_customer(
            arguments["customer_id"]
        )

    if name == "get_renewal_details":

        return get_renewal_details(
            arguments["customer_id"]
        )

    if name == "search_products":

        return search_products(
            arguments.get("category")
        )

    if name == "create_customer":

        return create_customer(
            arguments["name"],
            arguments["email"],
            arguments["phone"],
            arguments.get("dob"),
            arguments.get("city")
        )

    if name == "save_interest":

        return save_interest(
            arguments["customer_id"],
            arguments["category"]
        )

    return {
        "success": False,
        "message": f"Unknown tool: {name}"
    }

SYSTEM_INSTRUCTION = """
You are an AI customer service chatbot.

You help customers with:

1. Existing customer verification
2. Renewal information
3. Product discovery
4. New customer registration
5. Product interests

IMPORTANT RULES:

EXISTING CUSTOMER:

If the customer says they are an existing customer,
ask for their customer ID.

When they provide a customer ID,
use verify_customer.

Never invent customer information.

After successful verification, use the customer's
real information returned by the tool.

If the customer asks about renewal,
use get_renewal_details.

NEW CUSTOMER:

If the customer says they are a new customer,
collect:

- Name
- Email
- Phone

You may also collect:

- Date of birth
- City

Do not create a customer until the required
information is available.

After creating the customer,
tell the customer their generated customer ID.

PRODUCT INTEREST:

Ask what category the customer is interested in.

Save the interest using save_interest.

Then search products using search_products.

Do not invent product names, prices or customer information.

Only use information returned by the tools.

Be friendly, concise and professional.

Never expose internal Python functions,
database implementation or tool-calling details.
"""

def ask_ai(message, previous_interaction_id=None):

    user_input = message
    previous_id = previous_interaction_id

    while True:

       
        interaction = client.interactions.create(
            model=MODEL,
            input=user_input,
            previous_interaction_id=previous_id,
            system_instruction=(
                SYSTEM_INSTRUCTION
                if previous_id is None
                else None
            ),
            tools=tools
        )

        
        function_results = []

        if interaction.steps:

            for step in interaction.steps:

                if step.type == "function_call":

                    print("\n==============================")
                    print("AI TOOL CALL")
                    print("==============================")

                    print("Function:", step.name)
                    print("Arguments:", step.arguments)

                    
                    result = execute_tool(
                        step.name,
                        step.arguments
                    )

                    print("\nTOOL RESULT")
                    print(result)

                   
                    function_results.append({
                        "type": "function_result",
                        "name": step.name,
                        "call_id": step.id,
                        "result": [
                            {
                                "type": "text",
                                "text": json.dumps(result)
                            }
                        ]
                    })

        if not function_results:

            return interaction.output_text, interaction.id

        user_input = function_results

        previous_id = interaction.id