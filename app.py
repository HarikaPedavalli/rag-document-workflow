documents = [
    "RAG combines retrieval with generation for grounded responses.",
    "Chunking splits long text into smaller searchable units.",
    "Structured output helps make AI responses consistent."
]

def retrieve_context(query):
    matches = [doc for doc in documents if query.lower() in doc.lower()]
    return matches if matches else ["No relevant context found."]

def generate_response(query):
    context = retrieve_context(query)
    return {
        "query": query,
        "retrieved_context": context,
        "response": f"Generated answer using retrieved context: {context[0]}"
    }

if __name__ == "__main__":
    result = generate_response("RAG")
    print(result)
