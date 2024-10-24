from dotenv import load_dotenv, find_dotenv

import getpass
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    ChatPromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain


def terminal_chat(llm):

    # base_prompt = """
    #     {content}
    # """

    # prompt_template = HumanMessagePromptTemplate.from_template(base_prompt)
    # message_history = MessagesPlaceholder(variable_name="history")

    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # chat_prompt = ChatPromptTemplate.from_template(
    #     "The following is a conversation:\n{chat_history}\n\nHuman: {input}\nAI:"
    # )

    # # Create prompt template with message history
    # prompt = ChatPromptTemplate(
    #     input_variables=["content", "history"],
    #     messages=[message_history, prompt_template],
    # )

    # # Create the runnable sequence: memory and LLM combined
    # llm_chain = RunnableSequence([prompt, llm])

    # Define memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Define prompt template with memory for conversation context
    chat_prompt = ChatPromptTemplate.from_template(
        "The following is a conversation:\n{chat_history}\n\nHuman: {input}\nAI:"
    )

    # Create an LLM chain that includes memory
    llm_chain = LLMChain(llm=llm, prompt=chat_prompt, memory=memory)

    # Chat loop
    while True:
        user_prompt = input(">> ")
        result = llm_chain.run({"input": user_prompt})
        print(result)


if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)

    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-exp-0827",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ["GOOGLE_API_KEY"],
    )

    terminal_chat(llm)
