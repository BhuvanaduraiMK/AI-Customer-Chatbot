from ai_chatbot import client, MODEL, SYSTEM_INSTRUCTION, tools


response = client.interactions.create(
    model=MODEL,
    input="I am an existing customer. My customer ID is CUST1002.",
    system_instruction=SYSTEM_INSTRUCTION,
    tools=tools
)
