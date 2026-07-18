# 🤖 AI Customer Support Assistant | LangChain + Gemini + Streamlit

An AI-powered Customer Support Assistant built using LangChain, Google Gemini, and Streamlit. The application answers frequently asked customer questions, tracks orders, and provides professional responses using prompt engineering and a custom FAQ knowledge base.

---

## 📌 Features

- 🤖 AI-powered customer support chatbot
- 💬 Interactive Streamlit web interface
- 🧠 Prompt Engineering using LangChain Prompt Templates
- 📚 FAQ-based knowledge base
- 📦 Order tracking functionality
- 💳 Payment & refund assistance
- 🚚 Shipping information
- 🛡️ Warranty information
- 💾 Conversation history
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini API
- Streamlit
- python-dotenv

---

## 📂 Project Structure

```text
AI-Customer-Support-Assistant/
│
├── app.py
├── chatbot.py
├── prompts.py
├── knowledge_base.py
├── functions.py
├── data/
│   └── faq.txt
├── screenshots/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project

```bash
cd AI-Customer-Support-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## 💬 Sample Questions

- How long does shipping take?
- Can I track my order?
- Track my order ORD1002
- What is your return policy?
- How long do refunds take?
- What payment methods do you accept?
- What are your customer support hours?
- Do your products come with a warranty?

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Chat Interface
- Order Tracking Example

Place them inside the `screenshots` folder.

---

## 📈 Future Enhancements

- Database integration
- Real-time order tracking API
- PDF knowledge base support
- Voice-based customer support
- Multi-language support
- Authentication and user accounts
- LangChain tool calling
- Retrieval-Augmented Generation (RAG)

---

## 👨‍💻 Developed By

Varshaswi

Built as part of the Week 2 Internship Project on Prompt Engineering and LangChain.