import streamlit as st
from modules.vectore_store import load_model
from modules.retriever import retrieve_top_k
from modules.generator import generate_answer

# Charger le modèle
model = load_model()

# Titre de l'application
st.title("Générateur de Réponses sur le Basketball 🏀")

# Description
st.markdown(
    """
    Cette application utilise un modèle de traitement du langage pour répondre à vos questions sur le basketball. 
    Posez une question et obtenez une réponse basée sur un contexte extrait automatiquement.
    """
)

# Entrée utilisateur
query = st.text_input("Posez votre question sur le basketball :", "")

# Bouton pour soumettre la question
if st.button("Générer une réponse"):
    if query.strip():
        # Recherche des textes proches
        with st.spinner("Recherche des passages pertinents..."):
            results = retrieve_top_k(query, model, "faiss_basket.index", "basket_metadata.pkl", k=5)

        # Concaténer le contexte
        context = "\n\n".join(results["text"].tolist())

        # Générer la réponse
        with st.spinner("Génération de la réponse..."):
            response = generate_answer(context, query)

        # Afficher les résultats
        st.subheader("Contexte récupéré :")
        st.text_area("", context, height=200)

        st.subheader("Réponse générée :")
        st.success(response)
    else:
        st.error("Veuillez entrer une question valide.")