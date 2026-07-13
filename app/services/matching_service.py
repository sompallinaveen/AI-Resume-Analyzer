from sklearn.metrics.pairwise import cosine_similarity

from app.services.embedding_service import generate_embedding


def calculate_similarity(
    resume_text: str,
    job_description: str,
):
    resume_embedding = generate_embedding(resume_text)

    job_embedding = generate_embedding(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding],
    )[0][0]

    return round(float(similarity * 100), 2)