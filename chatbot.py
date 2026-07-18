import os
import re
import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from prompts import customer_support_prompt
from knowledge_base import load_faq
from functions import track_order

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

# Load FAQ
faq = load_faq()

# Create LangChain chain
chain = customer_support_prompt | llm | StrOutputParser()

# Store conversation history
conversation_history = []


def get_response(question):
    global conversation_history

    # -------- Function Calling Example --------
    # Detect order IDs like ORD1001, ORD1002, etc.
    match = re.search(r"ORD\d+", question.upper())

    if match and "track" in question.lower():
        return track_order(match.group())

    # ------------------------------------------

    history = "\n".join(conversation_history)

    result = chain.invoke(
        {
            "faq": faq,
            "history": history,
            "question": question,
        }
    )

    # Parse JSON response
    try:
        data = json.loads(result)
        answer = data.get("answer", result)
    except json.JSONDecodeError:
        answer = result

    # Save conversation history
    conversation_history.append(f"User: {question}")
    conversation_history.append(f"Assistant: {answer}")

    return answer