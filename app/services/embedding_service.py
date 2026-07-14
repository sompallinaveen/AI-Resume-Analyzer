from sentence_transformers import SentenceTransformer

model = None


def get_model():
    global model

    if model is None:
        print("Loading SentenceTransformer model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def generate_embedding(text: str):
    """
    Convert text into a semantic embedding.
    """
    model = get_model()
    return model.encode(text)