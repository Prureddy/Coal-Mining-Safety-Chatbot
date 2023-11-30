
from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
import json


# Load the configuration file
with open('config.json') as config_file:
    config = json.load(config_file)
    openai_api_key = config.get('openai_api_key')
    pinecone_api_key = config.get('pinecone_api_key')

# Set the OpenAI API key using the extracted key
openai.api_key = openai_api_key


# Initialize the SentenceTransformer model and Pinecone index
model = SentenceTransformer('all-MiniLM-L6-v2')
pinecone.init(api_key=pinecone_api_key, environment='gcp-starter')
index = pinecone.Index('langchain-chatbot')


def find_match(input):
    try:
        input_em = model.encode(input).tolist()
        result = index.query(input_em, top_k=2, includeMetadata=True)
        return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']
    except Exception as e:
        st.error("An error occurred during the match finding process: " + str(e))
        return ""


def query_refiner(conversation, query):
    """
    Use the OpenAI API to refine the given query based on the conversation log.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base strictly related to coal mines only.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        st.error("An error occurred during query refinement: " + str(e))
        return "An error occurred during query refinement"


def get_conversation_string():
    """
    Generate a conversation string from the stored conversation history.
    """
    try:
        conversation_string = ""
        for i in range(len(st.session_state['responses'])-1):
            conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
            conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
        return conversation_string
    except Exception as e:
        st.error("An error occurred while generating conversation string: " + str(e))
        return "An error occurred while generating conversation string"
