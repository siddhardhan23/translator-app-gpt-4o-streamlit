import os
import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# configure openai - api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o", temperature=0)


def translate(input_language, output_language, input_text):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
            ("human", "{input}")
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "input_language": input_language,
            "output_language": output_language,
            "input": input_text
        }
    )

    return response.content
