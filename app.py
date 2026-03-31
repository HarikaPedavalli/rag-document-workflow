import json

def read_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_text(text, chunk_size=80):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

def retrieve_context(query, chunks):
    query_words = query.lower().split()
    scored_chunks = []

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query_words)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])
    best_score, best_chunk = scored_chunks[0]

    if best_score == 0:
        return "No relevant context found."
    return best_chunk

def generate_response(query, context):
    return {
        "query": query,
        "retrieved_context": context,
        "response": f"Based on the retrieved context, the answer is: {context}"
    }

if __name__ == "__main__":
    document = read_document("sample_input.txt")
    chunks = chunk_text(document)
    context = retrieve_context("RAG retrieval", chunks)
    result = generate_response("RAG retrieval", context)

    print(json.dumps(result, indent=2))
