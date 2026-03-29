import pandas as pd
import numpy as np

def calculate_ECL(input_file, output_file):
    """
    Cette fonction :
    - Lit le CSV avec PD
    - Simule LGD et EAD
    - Calcule l'ECL
    - Sauvegarde le CSV avec les nouvelles colonnes
    """
    
    # 1️⃣ Lire le CSV avec PD
    df = pd.read_csv(input_file)
    
    # 2️⃣ Estimation de LGD (proportion de perte en cas de défaut)
    # Ici on simule entre 30% et 80%
    df['LGD'] = np.random.uniform(0.3, 0.8, len(df))
    
    # 3️⃣ Estimation de EAD (montant exposé au risque)
    # Pour simplifier, on prend encours_total comme EAD
    df['EAD'] = df['encours_total']
    
    # 4️⃣ Calcul de la perte attendue (ECL)
    df['ECL'] = df['PD'] * df['LGD'] * df['EAD']
    
    # 5️⃣ Sauvegarde du CSV enrichi
    df.to_csv(output_file, index=False)
    
    return df

# 6️⃣ Exécution directe si script lancé seul
if __name__ == "__main__":
    df_ECL = calculate_ECL(
        "data/processed/clients_scoring.csv",
        "data/processed/clients_ECL.csv"
    )
    print("✅ Calcul ECL terminé et CSV sauvegardé")