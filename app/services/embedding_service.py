from sentence_transformers import SentenceTransformer

# Load only once when the application starts
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text: str):
    """
    Convert text into a semantic embedding.
    """
    return model.encode(text)