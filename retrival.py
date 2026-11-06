import faiss
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text

def create_chunks(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def generate_embeddings(chunks):

    embeddings = model.encode(chunks)

    return np.array(embeddings).astype("float32")

def create_vector_database(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index

def retrieve_chunks(question, index, chunks, k=3):

    question_embedding = model.encode([question])

    question_embedding = np.array(
        question_embedding
    ).astype("float32")

    distances, indices = index.search(
        question_embedding,
        k=min(k, len(chunks))
    )

    results = []

    for i in indices[0]:

        results.append(chunks[i])

    return results

if __name__ == "__main__":

    text = extract_text("sample.pdf")

    chunks = create_chunks(text)

    embeddings = generate_embeddings(chunks)

    index = create_vector_database(embeddings)

    print("Total chunks:", len(chunks))

    question = input("\nAsk a question about your PDF: ")

    results = retrieve_chunks(question, index, chunks)

    print("\nRetrieved Results:")

    for i, result in enumerate(results):

        print(f"\n--- Result {i+1} ---")

        print(result)