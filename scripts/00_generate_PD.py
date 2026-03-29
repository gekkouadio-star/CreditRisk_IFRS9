import pandas as pd
import numpy as np

# Lire le fichier nettoyé
df = pd.read_csv("data/processed/clients_clean.csv")

# Générer une PD aléatoire pour chaque client (entre 0 et 0.2)
np.random.seed(42)  # pour reproductibilité
df['PD'] = np.random.uniform(0, 0.2, size=len(df))

# Sauvegarder
df.to_csv("data/processed/clients_clean.csv", index=False)
print("✅ Colonne PD ajoutée avec succès")