import pandas as pd
import re


# Fonction pour charger les données à partir d'un fichier CSV
def load_data(file_path):
    df = pd.read_csv(file_path, encoding="utf-8")
    # nettoyage des données
    def clean_text(text):
        if not isinstance(text, str):
            return ""

        text = re.sub(r"\s+", " ", text)   # Enlever les espaces supplémentaires
        return text
    
    # Appliquer la fonction de nettoyage à la colonne "content"
    df["text_clean"] = df["content"].apply(clean_text) 
    
    df_final = df[["title", "pageid", "text_clean"]].rename(columns={"text_clean": "text"}) # renommer la colonne "text_clean" en "text"
    
    return df_final
        


