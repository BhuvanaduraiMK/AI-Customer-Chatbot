<div align="center">

# 🤖 AI Customer Service Chatbot

### AI-Powered Customer Support & Product Assistant

<p>
  <strong>Chat • Verify • Renew • Register • Discover • Recommend</strong>
</p>

<p>
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3000&pause=800&color=0E75B6&center=true&vCenter=true&width=750&lines=AI+Customer+Service+Chatbot;Gemini-Powered+Customer+Support;Existing+Customer+Verification;New+Customer+Registration;Renewal+Information;AI+Product+Discovery" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python%20Dotenv-ECD53F?style=for-the-badge&logo=python&logoColor=black"/>
</p>

<p>
  <a href="https://github.com/BhuvanaduraiMK">
    <img src="https://img.shields.io/badge/GitHub-BhuvanaduraiMK-181717?style=for-the-badge&logo=github"/>
  </a>
  <a href="https://www.linkedin.com/in/bhuvanadurai-m-1312a7248/">
    <img src="https://img.shields.io/badge/LinkedIn-Bhuvanadurai%20M-0077B5?style=for-the-badge&logo=linkedin"/>
  </a>
</p>

</div>

---

# 📌 About the Project

**AI Customer Service Chatbot** is an AI-powered customer support application built using **Python, Streamlit, Google Gemini and SQLite**.

The chatbot is designed to handle two major customer types:

- 👤 Existing Customers
- 🆕 New Customers

Instead of using only traditional rule-based chatbot logic, the system uses **Gemini AI with function/tool calling** to understand customer requests and interact with backend database functions.

The chatbot can verify customers, retrieve renewal information, register new customers, save product interests and search products based on customer requirements.

---

# 🎯 Project Objective

Traditional customer service systems often depend on predefined menus and rigid rule-based flows.

For example:

```text
Enter 1 for Existing Customer
Enter 2 for New Customer
Enter 3 for Products
```
Simple workflow
```
                 Customer
                     │
                     ▼
              Streamlit Chat UI
                     │
                     ▼
                Gemini AI
                     │
             Tool / Function
                Calling
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   Customer       Renewal      Products
 Verification     Details       Search
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
               SQLite Database
                     │
                     ▼
                Tool Result
                     │
                     ▼
                 Gemini AI
                     │
                     ▼
             Natural Language
                Response
```

👥 Customer Types

The chatbot supports two primary customer flows.
| Customer Type        | Main Operations                                                         |
| -------------------- | ----------------------------------------------------------------------- |
| 👤 Existing Customer | Verify ID, view renewals, explore products                              |
| 🆕 New Customer      | Register account, generate Customer ID, save interest, explore products |

✨ Key Features
👤 1. Existing Customer Verification

Existing customers can provide their Customer ID.

Example:
```
User:
I am an existing customer.

AI:
Sure! Please provide your Customer ID.

User:
CUST1002
```

Gemini identifies that customer verification is required and calls:
```
verify_customer()
```

The backend checks the SQLite database.
```
Customer ID: CUST1002
Name: Swetha
Email: swetha@gmail.com
Phone: 9876543211
City: Bangalore
```
🔄 2. Renewal Information

After successful customer verification, the customer can ask about renewals.

Example:
```
User:
Show my renewal details.
```
Gemini calls:
```
get_renewal_details()
```
The backend retrieves renewal information from SQLite.

Example response:
```
Home Appliances
Expiry Date: September 10, 2026
Renewal Amount: ₹3000

Electronics Package
Expiry Date: November 15, 2026
Renewal Amount: ₹5000
```
🛍️ 3. Product Discovery

Customers can ask about available products.

Example:

```User:
I am interested in sports products.
```

Gemini can identify the customer's interest and use:

```search_products()
```

The database returns matching products.

Example:
```
Product:
Sports Equipment

Category:
Sports

Price:
₹2500

Description:
High-quality sports equipment
```

❤️ 4. Customer Interest Management

The chatbot can save the customer's product interest.

Function:
```
save_interest()
```
Example:
```
Customer ID:
CUST1002

Interest:
Sports
```
🆕 5. New Customer Registration

New customers can register through natural conversation.

Example:
```
User:
I am a new customer.

AI:
I'll help you create an account.
What's your name?

User:
Arun Kumar

AI:
What's your email?

User:
arun@gmail.com

AI:
What's your phone number?

User:
9876543210
```
🆔 6. Automatic Customer ID Generation

When a new customer is created, the backend automatically generates a Customer ID.

Example:
```
CUST1003
```
The chatbot then informs the customer:
```
Welcome, Arun Kumar!

Your account has been created successfully.

Your Customer ID is CUST1003.
```

🤖 7. Gemini Function / Tool Calling

One of the main technical features of this project is Gemini function calling.

Instead of allowing the AI to directly manipulate the database, the AI decides which backend function is required.

Available tools:
```
verify_customer()
get_renewal_details()
search_products()
create_customer()
save_interest()
```
Example:
```
User
 │
 │ "Show my renewal details"
 ▼
Gemini AI
 │
 │ Function Call
 ▼
get_renewal_details()
 │
 ▼
SQLite Database
 │
 ▼
Renewal Data
 │
 ▼
Gemini AI
 │
 ▼
Natural Language Response
```

🧠 AI Architecture

The chatbot follows a tool-based AI architecture.

```
┌───────────────────────────────────────┐
│              User                     │
│                                       │
│ "Show my renewal details"             │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│          Streamlit Chat UI            │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│             Gemini AI                 │
│                                       │
│ Understands user intent               │
│ Selects appropriate tool              │
└──────────────────┬────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │    Tool Selection    │
        └──────────┬───────────┘
                   │
       ┌───────────┼────────────┐
       ▼           ▼            ▼
  verify_       get_renewal   search_
 customer()     _details()    products()
       │           │            │
       └───────────┼────────────┘
                   ▼
          Database Tools
                   │
                   ▼
              SQLite DB
                   │
                   ▼
             Tool Result
                   │
                   ▼
              Gemini AI
                   │
                   ▼
          Final AI Response
```
🗃️ Database

The project uses SQLite as the database.

The database contains information related to:

Customers
```
customer_id
name
email
phone
dob
city
```
Products
```
product_id
product_name
category
price
description
```
Renewals
```
renewal_id
customer_id
product_name
expiry_date
renewal_amount
```
🛠️ Technology Stack
---
🐍 Backend
<p> <img src="https://skillicons.dev/icons?i=python"/> </p>
Python
SQLite
Python-dotenv

---

🌐 User Interface
<p> <img src="https://skillicons.dev/icons?i=streamlit"/> </p>
Streamlit
Streamlit Chat Components
Custom UI styling

---

🤖 Generative AI
Google Gemini API
Gemini Function Calling
Natural Language Understanding
Tool-based AI architecture
Multi-turn conversations

---


🗄️ Database
SQLite
SQL

---

Database helper functions
🧰 Development Tools
<p> <img src="https://skillicons.dev/icons?i=git,github,vscode"/> </p>
Git
GitHub
Visual Studio Code
Python Virtual Environment

---
📁 Project Structure
```
AI_Customer_Chatbot/
│
├── app.py
│
├── ai_chatbot.py
│
├── database.py
│
├── database_tools.py
│
├── test_ai.py
│
├── test_database_tools.py
│
├── requirements.txt
│
├── .env.example
│
├── .gitignore
│
└── README.md
```

File Responsibilities
| File                     | Responsibility                    |
| ------------------------ | --------------------------------- |
| `app.py`                 | Streamlit chatbot interface       |
| `ai_chatbot.py`          | Gemini AI and function calling    |
| `database.py`            | Database creation and sample data |
| `database_tools.py`      | Database operations used by AI    |
| `test_ai.py`             | AI and tool-calling tests         |
| `test_database_tools.py` | Database function tests           |
| `.env.example`           | Environment variable template     |
| `requirements.txt`       | Python dependencies               |


⚙️ Installation & Setup
---
1. Clone the Repository
```
git clone https://github.com/BhuvanaduraiMK/AI_Customer_Chatbot.git
cd AI_Customer_Chatbot
```
---
🐍 2. Create Virtual Environment

Windows:
```
python -m venv venv
```
---

Activate:
```
venv\Scripts\activate
```

📦 3. Install Dependencies
```
pip install -r requirements.txt
```

🔐 Environment Variables

Create a .env file in the project root.
```
GEMINI_API_KEY=your_gemini_api_key
```

🗄️ 4. Initialize the Database
```
python database.py
```
🧪 5. Test Database Tools

Run:
```
python test_database_tools.py
```
The test verifies:
```
✓ Customer verification
✓ Renewal details
✓ Product search
✓ Customer interest saving
```

🤖 6. Test Gemini AI

Run:
```
python test_ai.py
```
The test verifies:
```
✓ Gemini connection
✓ AI response
✓ Function calling
✓ Tool execution
✓ Database result processing
✓ Final AI response
```
🚀 7. Run the Application

Start Streamlit:
```
streamlit run app.py
```
The chatbot will open in the browser.

🔄 Application Workflow
```
                 Start
                   │
                   ▼
              Chatbot UI
                   │
                   ▼
             User Message
                   │
                   ▼
              Gemini AI
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
 Existing Customer       New Customer
          │                  │
          ▼                  ▼
   Customer ID          Personal Data
          │                  │
          ▼                  ▼
 verify_customer()     create_customer()
          │                  │
          ▼                  ▼
 Customer Verified      Customer ID
          │                  │
          └────────┬─────────┘
                   │
                   ▼
            Product Interest
                   │
                   ▼
             save_interest()
                   │
                   ▼
            search_products()
                   │
                   ▼
             Product Results
                   │
                   ▼
              Gemini AI
                   │
                   ▼
             Final Response
```

💬 Example Conversations
👤 Existing Customer
```
User:
I am an existing customer.

AI:
Sure! Please provide your Customer ID.

User:
CUST1002

AI:
Hello Swetha! Your account has been successfully verified.
```
🔄 Renewal Example
```
User:
Show my renewal details.

AI:
Here are your upcoming renewals:

Home Appliances
Expiry Date: September 10, 2026
Renewal Amount: ₹3000

Electronics Package
Expiry Date: November 15, 2026
Renewal Amount: ₹5000
```
🆕 New Customer
```
User:
I am a new customer.

AI:
I'll help you create an account.
What's your name?

User:
Arun Kumar

AI:
What's your email?

User:
arun@gmail.com

AI:
What's your phone number?

User:
9876543210
```
🛍️ Product Interest
```
User:
I am interested in sports.

AI:
Your interest has been saved.

Here's a product available in the Sports category:

Sports Equipment
Price: ₹2500
```
🧪 Testing

The project was tested using different chatbot scenarios.
Existing Customer
```
✓ Valid Customer ID
✓ Invalid Customer ID
✓ Customer verification
✓ Renewal information
```
New Customer
```
✓ Personal information collection
✓ Customer creation
✓ Automatic Customer ID generation
```
Product Discovery
```
✓ Product category search
✓ Interest saving
✓ Product retrieval
```
---
🎯 Project Highlights
🤖 AI-Powered Customer Service

Uses Gemini AI to understand natural-language customer requests.
---
🔧 Function Calling

Gemini can select backend functions based on the user's intent.
---
🗃️ Database Integration

Customer and product information is retrieved from SQLite rather than being invented by the AI.
---
👥 Two Customer Flows

Supports both existing customer verification and new customer registration.
---
🆔 Automatic Customer ID

New customers receive a generated Customer ID after registration.
---
💬 Conversational Experience

The chatbot supports multi-turn conversations instead of relying only on fixed menus.
---
🛍️ Product Discovery

Customers can express their interests and receive matching products from the database.

---

🚀 Future Enhancements

Possible future improvements include:

🔐 User Authentication

🗄️ PostgreSQL / MySQL Integration

📊 Admin Dashboard

🛍️ Advanced Product Recommendation

📦 Order Management

💳 Payment Integration

📧 Email Notifications

📱 Mobile-Friendly Interface

☁️ Cloud Deployment

🐳 Docker Containerization

📈 Customer Analytics

🧠 Personalized AI Recommendations

📝 Conversation History

---

👨‍💻 About the Developer
Bhuvanadurai M

🎓 Computer Science & Engineering — Data Science

💡 Interested in:

Artificial Intelligence
Machine Learning
Data Science
Data Engineering
Generative AI
Backend Development
Database Systems

🚀 Building practical AI and data-driven applications.

🎯 Career Goal:

AI-ML Engineer / Data Engineer

---

Connect With Me
<p align="center"> <a href="https://github.com/BhuvanaduraiMK"> <img src="https://img.shields.io/badge/GitHub-BhuvanaduraiMK-181717?style=for-the-badge&logo=github"/> </a> <a href="https://www.linkedin.com/in/bhuvanadurai-m-1312a7248/"> <img src="https://img.shields.io/badge/LinkedIn-Bhuvanadurai%20M-0077B5?style=for-the-badge&logo=linkedin"/> </a> </p>
---

⭐ Support

If you find this project useful or interesting, consider giving it a ⭐ on GitHub.

<p align="center">

🤖 Built with Python, Streamlit, SQLite & Gemini AI

⭐ Thanks for visiting the AI Customer Service Chatbot!

</p> ```


