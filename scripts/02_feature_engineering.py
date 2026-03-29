import pandas as pd  # Librairie pour manipuler les DataFrame

def create_features(input_file, output_file):
    """
    Cette fonction lit un CSV nettoyé, crée de nouvelles variables,
    puis sauvegarde le CSV enrichi.
    """
    
    # 1️⃣ Lire le fichier nettoyé
    df = pd.read_csv(input_file)
    
    # 2️⃣ Créer une nouvelle feature : taux d'endettement
    #    taux_endettement = encours_total / revenu_mensuel
    df['taux_endettement'] = df['encours_total'] / df['revenu_mensuel']
    
    # 3️⃣ Sauvegarder le CSV enrichi
    df.to_csv(output_file, index=False)
    
    # 4️⃣ Retourner le DataFrame pour un usage immédiat
    return df

# 5️⃣ Exécution directe si le script est lancé seul
if __name__ == "__main__":
    df_features = create_features(
        "data/processed/clients_clean.csv",
        "data/processed/clients_features.csv"
    )
    print("✅ Features créées et fichier sauvegardé")