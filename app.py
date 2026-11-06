import streamlit as st

from retrival import (
    extract_text,
    create_chunks,
    generate_embeddings,
    create_vector_database,
    retrieve_chunks
)

from generation import generate_answer


# Page configuration
st.set_page_config(
    page_title="Mini RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Chat with Your PDF")

st.write("Upload a PDF and ask questions about its content.")


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None


# Sidebar
with st.sidebar:

    st.header("Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button("Process PDF"):

            with st.spinner("Processing document..."):

                # Extract text
                from pypdf import PdfReader

                reader = PdfReader(uploaded_file)

                text = ""

                for page in reader.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

                # Chunking
                chunks = create_chunks(text)

                # Embeddings
                embeddings = generate_embeddings(chunks)

                # FAISS
                index = create_vector_database(embeddings)

                st.session_state.index = index

                st.session_state.chunks = chunks

                st.session_state.messages = []

            st.success("PDF processed successfully!")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask something about your PDF...")

if question:

    if st.session_state.index is None:

        st.warning("Please upload and process a PDF first.")

    else:

        # Display user question
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        # Retrieval
        results = retrieve_chunks(
            question,
            st.session_state.index,
            st.session_state.chunks,
            k=3
        )

        context = "\n\n".join(results)

        # Generation
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = generate_answer(
                    question,
                    context
                )

                st.markdown(answer)

                with st.expander("View retrieved sources"):

                    for i, chunk in enumerate(results):

                        st.write(f"Source {i+1}")

                        st.write(chunk)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })