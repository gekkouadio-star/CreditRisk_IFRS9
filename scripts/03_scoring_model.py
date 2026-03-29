import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def build_PD_model(input_file, output_file):
    """
    Cette fonction :
    - Lit le CSV avec les features
    - Entraîne un modèle de scoring PD (logistic regression)
    - Calcule les PD pour tous les clients
    - Sauvegarde le CSV enrichi
    """
    
    # 1️⃣ Lecture du CSV avec les features
    df = pd.read_csv(input_file)
    
    # 2️⃣ Définition des variables
    X = df[['taux_endettement','anciennete_client']]  # variables explicatives
    y = df['defaut']                                 # variable cible (0 ou 1)
    
    # 3️⃣ Séparation Train/Test (20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 4️⃣ Création et entraînement du modèle de régression logistique
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 5️⃣ Calcul des probabilités de défaut pour tous les clients
    df['PD'] = model.predict_proba(X)[:,1]  # [:,1] = probabilité de classe 1 (défaut)
    
    # 6️⃣ Évaluation du modèle avec AUC
    auc = roc_auc_score(y, df['PD'])
    print(f"AUC PD: {auc:.3f}")
    
    # 7️⃣ Sauvegarde du CSV avec PD
    df.to_csv(output_file, index=False)
    
    return df, model

# 8️⃣ Exécution directe si le script est lancé seul
if __name__ == "__main__":
    df_scoring, model = build_PD_model(
        "data/processed/clients_features.csv",
        "data/processed/clients_scoring.csv"
    )
    print("✅ Modèle PD construit et CSV sauvegardé")