import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # pour vérifier/créer le dossier
import numpy as np  # pour générer LGD et EAD simulés

def create_dashboard(input_file, figures_folder="reports/figures/"):
    """
    Cette fonction :
    - Lit le CSV final avec PD et Stage_IFRS9
    - Calcule LGD, EAD et ECL si elles n'existent pas
    - Crée plusieurs graphiques pour le reporting
    - Sauvegarde les figures au format PNG
    """
    
    # 0️⃣ Créer le dossier s'il n'existe pas
    os.makedirs(figures_folder, exist_ok=True)
    
    # 1️⃣ Lire le CSV final
    df = pd.read_csv(input_file)
    print(f"✅ CSV chargé : {input_file}")
    
    # 1️⃣b Vérifier si LGD/EAD/ECL existent, sinon les créer
    if 'LGD' not in df.columns:
        np.random.seed(42)
        df['LGD'] = np.random.uniform(0.3, 0.7, size=len(df))  # 30%-70%
        print("ℹ️ Colonne LGD créée")
    if 'EAD' not in df.columns:
        df['EAD'] = df['encours_total']  # simplification : exposé = encours total
        print("ℹ️ Colonne EAD créée")
    if 'ECL' not in df.columns:
        df['ECL'] = df['PD'] * df['LGD'] * df['EAD']
        print("ℹ️ Colonne ECL calculée")
    
    # 2️⃣ Histogramme des PD
    plt.figure(figsize=(8,5))
    sns.histplot(df['PD'], bins=30, kde=True, color='skyblue')
    plt.title("Distribution des Probabilités de Défaut (PD)")
    plt.xlabel("PD")
    plt.ylabel("Nombre de clients")
    plt.savefig(f"{figures_folder}PD_distribution.png")
    plt.close()
    
    # 3️⃣ Histogramme des ECL
    plt.figure(figsize=(8,5))
    sns.histplot(df['ECL'], bins=30, color='salmon')
    plt.title("Distribution des pertes attendues (ECL)")
    plt.xlabel("ECL")
    plt.ylabel("Nombre de clients")
    plt.savefig(f"{figures_folder}ECL_distribution.png")
    plt.close()
    
    # 4️⃣ Répartition des stages IFRS9
    plt.figure(figsize=(6,6))
    df['Stage_IFRS9'].value_counts().sort_index().plot.pie(
        autopct="%1.1f%%", colors=['green','orange','red']
    )
    plt.title("Répartition Stage IFRS9")
    plt.ylabel("")
    plt.savefig(f"{figures_folder}Stage_IFRS9_pie.png")
    plt.close()
    
    # 5️⃣ Sauvegarder CSV mis à jour
    df.to_csv(input_file, index=False)
    print(f"✅ Dashboard généré et figures sauvegardées dans {figures_folder}")
    print(f"✅ CSV mis à jour sauvegardé : {input_file}")

# 6️⃣ Exécution directe
if __name__ == "__main__":
    create_dashboard("data/processed/clients_IFRS9.csv")