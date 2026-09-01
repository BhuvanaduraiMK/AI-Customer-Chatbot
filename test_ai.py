from ai_chatbot import ask_ai


message = """
I am an existing customer with customer ID CUST1002.
I am interested in Sports products.
Please save my interest and show me the available products.
"""


response = ask_ai(message)


print("\n==============================")
print("FINAL AI RESPONSE")
print("==============================")

print(response)