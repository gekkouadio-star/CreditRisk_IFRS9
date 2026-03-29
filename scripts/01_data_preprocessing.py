import pandas as pd  # Librairie pour manipuler les données

def clean_data(input_file, output_file):
    # Charger le CSV brut
    df = pd.read_csv(input_file)
    
    # Supprimer les doublons
    df = df.drop_duplicates()
    
    # Remplacer les valeurs manquantes par 0 (simplification)
    df = df.fillna(0)
    
    # Sauvegarder le CSV nettoyé
    df.to_csv(output_file, index=False)
    
    return df

# Exécution directe si le script est lancé seul
if __name__ == "__main__":
    df_clean = clean_data("data/raw/clients_bancaires_5000.csv",
                          "data/processed/clients_clean.csv")
    print("✅ Nettoyage terminé. Fichier sauvegardé dans processed/")