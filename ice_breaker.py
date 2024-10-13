from dotenv import load_dotenv, find_dotenv

import getpass
import os

from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import linkedin_profile_json


def translate(llm):

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to Turkish. Translate the user sentence.",
        ),
        ("human", "GIST OF LANGCHAIN"),
    ]

    ai_msg = llm.invoke(messages)

    print(ai_msg.content)


def suummarize(llm):
    summary_template = """
    You are a very good assistant that summarizes texts.
    Please summarize the information in 1 sentece: {information}
    """

    # Create a PromptTemplate object from the template and input variables
    summary_prompt_template = PromptTemplate.from_template(summary_template)

    summary_chain = summary_prompt_template | llm | StrOutputParser()

    summary_information = """
            LangChain is a framework for developing applications powered by language models.
            It provides a simple interface for interacting with a variety of language models,
            including OpenAI's GPT-3 and GPT-4, Anthropic's Claude, and more.
            LangChain also provides a range of tools and utilities for common tasks in language model applications,
            such as text generation, question answering, and summarization.
            """

    summary_message = summary_chain.invoke(input={"information": summary_information})

    print(summary_message)


def give_information_about_a_person(llm):

    information_template = """
    You are a very good assistant that gives information about a person. I will give you linkedin account data of that person in json format.
    Please give information about the person: {person}

    1. Short summary of the person
    2. Two interesting facts about the person
    3. 1 sentence about the person's impact on the world
    """

    # Create a PromptTemplate object from the template and input variables
    information_prompt_template = PromptTemplate.from_template(information_template)

    information_chain = information_prompt_template | llm | StrOutputParser()

    linkedin_data = linkedin_profile_json()

    information_message = information_chain.invoke(input={"person": linkedin_data})

    print(information_message)


if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)

    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-exp-0827",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ["GOOGLE_API_KEY"],
        # other params...
    )

    # llm = ChatOllama(model="tinyllama", temperature=0)

    # translate(llm)
    # suummarize(llm)
    # give_information_about_a_person(llm)
