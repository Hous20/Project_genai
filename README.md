# Project GenAI : Assistant de Réponses sur le Basketball 🏀

## Description du Projet

Ce projet est un système de Question-Réponse spécialisé dans le domaine du basketball. Il utilise des techniques avancées de NLP (Natural Language Processing) et de RAG (Retrieval Augmented Generation) pour fournir des réponses précises et pertinentes à des questions sur le basketball en se basant sur des données extraites de Wikipédia.

## Fonctionnalités

- **Recherche Sémantique** : Utilisation d'embeddings vectoriels pour trouver les passages les plus pertinents en fonction d'une question.
- **Extraction de Contexte** : Récupération des textes les plus similaires à la requête de l'utilisateur.
- **Génération de Réponses** : Utilisation du modèle Mistral via Ollama pour générer des réponses basées sur le contexte extrait.
- **Interface Web** : Interface utilisateur simple créée avec Streamlit permettant de poser des questions et d'obtenir des réponses.

## Architecture du Projet

Le projet est organisé selon la structure suivante :

```
Project_genai/
├── app.py                  # Application Streamlit principale
├── requirements.txt        # Dépendances du projet
├── data/                   # Données utilisées par l'application
│   └── wikipedia_basketball_articles.csv  # Données extraites de Wikipédia
└── modules/                # Modules et composants du système
    ├── __init__.py
    ├── data_loader.py      # Chargement et prétraitement des données
    ├── faiss_indexeur.py   # Gestion de l'index FAISS pour la recherche vectorielle
    ├── generator.py        # Génération de réponses avec le modèle Mistral (Ollama)
    ├── retriever.py        # Récupération des passages pertinents
    ├── scrapping.py        # Extraction des données depuis Wikipédia
    └── vectore_store.py    # Manipulation des vecteurs et embeddings
```

## Prérequis

- Python 3.8 ou supérieur
- Ollama installé localement avec le modèle Mistral
- Dépendances Python listées dans `requirements.txt`

## Installation

1. Clonez le dépôt :
```
git clone https://github.com/Hous20/Project_genai.git
cd Project_genai
```

2. Installez les dépendances :
```
pip install -r requirements.txt
```

3. Assurez-vous que Ollama est installé et que le modèle Mistral est disponible :
```
ollama pull mistral
```

## Utilisation

1. Pour collecter des données de Wikipédia (déjà disponibles dans le répertoire `data/`) :
```
python -m modules.scrapping
```

2. Pour créer l'index FAISS à partir des articles (à faire une seule fois) :
```
# Créez un script build_index.py avec le code approprié utilisant les fonctions de faiss_indexeur.py
```

3. Pour lancer l'application :
```
streamlit run app.py
```

4. Visitez l'URL locale indiquée (généralement http://localhost:8501) et posez vos questions sur le basketball.

## Fonctionnement

1. L'utilisateur pose une question via l'interface Streamlit.
2. Le système convertit la question en vecteur d'embeddings à l'aide du modèle SentenceTransformer.
3. L'index FAISS est utilisé pour trouver les passages les plus similaires à la question.
4. Ces passages sont compilés pour former un contexte pertinent.
5. Le modèle Mistral (via Ollama) génère une réponse en fonction de ce contexte et de la question originale.

## Technologies Utilisées

- **Streamlit** : Interface utilisateur web
- **SentenceTransformers** : Création d'embeddings vectoriels
- **FAISS** : Index vectoriel pour la recherche de similarité
- **Pandas** : Manipulation des données
- **BeautifulSoup & Requests** : Extraction de données web
- **Ollama** : Interface pour les modèles de langage locaux
- **Mistral** : Modèle de génération de texte

## Auteurs

- [Hous20](https://github.com/Hous20)

## Licence

Ce projet est sous licence [LICENSE].