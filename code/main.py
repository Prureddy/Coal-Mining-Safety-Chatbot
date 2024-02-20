    from langchain.chat_models import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.chains.conversation.memory import ConversationBufferWindowMemory
    from langchain.prompts import (
        SystemMessagePromptTemplate,
        HumanMessagePromptTemplate,
        ChatPromptTemplate,
        MessagesPlaceholder
    )
    import streamlit as st
    from streamlit_option_menu import option_menu
    from streamlit_chat import message
    from utils import *

    import json

    st.header("KhaanVaaniii")

    # Your existing code for initializing variables and Streamlit setup...

    try:
        if 'responses' not in st.session_state:
            st.session_state['responses'] = ["Have a Good day!, How can I assist you?"]

        if 'requests' not in st.session_state:
            st.session_state['requests'] = []

        with open('config.json') as config_file:
            config = json.load(config_file)
            api_key = config.get('openai_api_key', None)
            
        if api_key is None:
            st.error("API key is missing. Please provide a valid API key in the config.json file.")
            st.stop()
        else:
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key)

            if 'buffer_memory' not in st.session_state:
                st.session_state.buffer_memory = ConversationBufferWindowMemory(k=5, return_messages=True)
    except ValueError:
        st.error("Incorrect API key provided. Please check and update the API key in the config.json file.")
        st.stop()
    except Exception as e:
        st.error("An error occurred during initialization: " + str(e))
        llm = None
        st.session_state.buffer_memory = None

    # The rest of your Streamlit app code...


    system_msg_template = SystemMessagePromptTemplate.from_template(
        template="""Answer the question as truthfully as possible using the provided context, 
        and if the answer is not contained within the text below, say 'I don't know'"""
    )

    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

    conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

    # container for chat history
    response_container = st.container()
    # container for text box
    textcontainer = st.container()


    with textcontainer:
        query = st.text_input("Query: ", key="input")
        # Within the block where you handle user queries and generate responses
    if query:
        with st.spinner("typing..."):
            try:
                conversation_string = get_conversation_string()
                refined_query = query_refiner(conversation_string, query)
                st.subheader("Refined Query:")
                st.write(refined_query)
                context = find_match(query)
                
                # Check if the context pertains to coal mining before generating a response
                if "coal" in context.lower() or "mine" in context.lower() or "hi" in context.lower() or "hello" in context.lower() or "hey" in context.lower():
                    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
                    st.session_state.requests.append(query)
                    st.session_state.responses.append(response)
                else:
                    st.warning("This query is not related to coal mining. Please ask a question about coal mines.")
                    
            except Exception as e:
                st.error("An error occurred during conversation: " + str(e))


    with response_container:
        if st.session_state['responses']:
            for i in range(len(st.session_state['responses'])):
                try:
                    message(st.session_state['responses'][i], key=str(i))
                    if i < len(st.session_state['requests']):
                        message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')
                except Exception as e:
                    st.error("An error occurred while displaying messages: " + str(e))


    with st.sidebar:
        st.title("KhaanVaani")
        selected = option_menu(
            menu_title="None",
            options=["Home", "Projects", "Contacts"],
        )
        
    if selected == "Home":
        st.title(f"Home dude")
    if selected == "Projects":
        st.title(f"Projects Dude")

