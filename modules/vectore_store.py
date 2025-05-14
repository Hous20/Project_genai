from sentence_transformers import SentenceTransformer
import numpy as np

def load_model(model_name="all-MiniLM-L6-v2"):
    """
    Charge le modèle d embedding SentenceTransformer.
    
    Args:
        model_name (str): Le nom du modèle à charger.
        
    Returns:
        model: Le modèle SentenceTransformer chargé.
    """
    model = SentenceTransformer(model_name)
    return model


def compute_embeddings(model, texts):
    """
    Calcule les embeddings pour une liste de textes.
    
    Args:
        model: Le modèle SentenceTransformer.
        texts (list): Liste de textes à encoder.
        
    Returns:
        np.ndarray: Matrice d embeddings.
    """
    embeddings = model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)
