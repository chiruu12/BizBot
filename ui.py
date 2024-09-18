import streamlit as st
from rag_chain import RAG_Chain  

st.set_page_config(page_title='QA ChatBot', layout='wide', initial_sidebar_state='expanded')

    
st.sidebar.markdown(
    """
    <style>
        .sidebar-header {
            font-size: 30px; /* Adjust the font size as needed */
            font-weight: bold;
            color: #789; /* Adjust the color as needed */
            margin-bottom: 20px; /* Space below the header */
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<div class="sidebar-header">BizBot 📈</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'option' not in st.session_state:
    st.session_state['option'] = 'none'

uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
if st.sidebar.button("Clear Chat", key="clear_chat", help="Clear conversation history"):
    st.session_state.messages = []

def main():
    # Initializing the RAGChain
    chain = RAG_Chain()
    rag_chain = chain.get_rag_chain()
    if uploaded_file:
        chain.update_vectorstore_with_files(file=uploaded_file)  # Update vector store with the uploaded file it wont be updated if no file is uploaded 

    # Display messages in the chat area
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if query:= st.chat_input("Please ask your Query?"):
        st.session_state.messages.append({"role": "user", "content": query})  # Add user query to session state(messages)
        with st.chat_message("user"):
            st.markdown(query)  # Display user query
            
        with st.chat_message("assistant") and st.spinner('Processing...'):
            try:
                response = rag_chain.invoke({"input": query})
                answer = response["answer"]  # only getting the answer from the response as it is a dictionary  
                response = st.write(answer) 
                st.session_state.messages.append({"role": "assistant", "content": answer}) # Add assistant's answer to session state(messages)
            except Exception as e:
                st.error(f"An error occurred: {e}")  # Shows error if something goes wrong

if __name__ == "__main__":
    main()