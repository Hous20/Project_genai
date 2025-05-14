from .vectore_store import compute_embeddings
from .faiss_indexeur import load_faiss_index

def retrieve_top_k(query, model, faiss_index_path, metadata_path, k=5):
    """
    À partir d'une question, récupère les K passages les plus proches.
    """
    # Charger l'index et les métadonnées
    index, metadata = load_faiss_index(faiss_index_path, metadata_path)

    # Encoder la question
    query_embedding = compute_embeddings(model, [query])[0].reshape(1, -1)

    # Recherche dans l’index
    distances, indices = index.search(query_embedding, k)

    # Récupération des textes associés
    retrieved = metadata.iloc[indices[0]]
    return retrieved
