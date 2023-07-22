import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=api_key)

# doesn't work because needs different types
# chat('tell me a joke')

from langchain.schema import AIMessage, HumanMessage, SystemMessage

result = chat([
    SystemMessage(content="you are a conservative who hates the environment \
                and has strong feelings on global warming. also, you have \
                a penchant for cursing and referencing mainstream \
                conservative news channels"),
    HumanMessage(content="how do you feel about global warming?")
    ])


print(result)