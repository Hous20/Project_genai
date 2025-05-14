import faiss 
import pickle

def build_faiss_index(embeddings, dim):
    """"Créer un index FAISS à partir des embeddings."""
    index = faiss.IndexFlatL2(dim)  # Utiliser la distance euclidienne
    index.add(embeddings)  # Ajouter les embeddings à l'index
    return index

def save_faiss_index(index, path_index, path_metadata, metadata):
    """Sauvegarder l'index FAISS et les métadonnées."""
    faiss.write_index(index, path_index)  # Sauvegarder l'index
    with open(path_metadata, 'wb') as f:
        pickle.dump(metadata, f)  # Sauvegarder les métadonnées
    print(f"Index et métadonnées sauvegardés dans {path_index} et {path_metadata}")
    
def load_faiss_index(path_index, path_metadata):
    """Charger l'index FAISS et les métadonnées."""
    index = faiss.read_index(path_index)  # Charger l'index
    with open(path_metadata, 'rb') as f:
        metadata = pickle.load(f)  # Charger les métadonnées
    print(f"Index et métadonnées chargés depuis {path_index} et {path_metadata}")
    return index, metadata