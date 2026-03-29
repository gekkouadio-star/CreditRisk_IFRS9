import pandas as pd
import numpy as np

# --- 1️⃣ Lire le fichier brut ---
input_file = "data/raw/clients_bancaires_5000.csv"
df = pd.read_csv(input_file)
print("✅ CSV brut chargé")

# --- 2️⃣ Nettoyage simple ---
df = df.drop_duplicates()        # Supprimer doublons
df = df.fillna(0)                # Remplacer valeurs manquantes
print("✅ Nettoyage terminé")

# --- 3️⃣ Générer PD simulée ---
np.random.seed(42)
df['PD'] = np.random.uniform(0, 0.2, size=len(df))
print("✅ Colonne PD ajoutée")

# --- 4️⃣ Classifier IFRS9 ---
def get_stage(row):
    if row['PD'] >= 0.10:
        return 3
    elif row['PD'] >= 0.02:
        return 2
    else:
        return 1

df['Stage_IFRS9'] = df.apply(get_stage, axis=1)
print("✅ Classification IFRS9 terminée")

# --- 5️⃣ Sauvegarder CSV final ---
output_file = "data/processed/clients_IFRS9.csv"
df.to_csv(output_file, index=False)
print(f"✅ Fichier final sauvegardé : {output_file}")