import pandas as pd
import numpy as np

np.random.seed(42)
n_clients = 5000

df = pd.DataFrame({
    "client_id": range(1, n_clients+1),
    "revenu_mensuel": np.random.normal(4000, 1500, n_clients).clip(1000, 15000),
    "encours_total": np.random.normal(15000, 5000, n_clients).clip(1000, 100000),
    "anciennete_client": np.random.randint(1, 20, n_clients),
    "defaut": np.random.binomial(1, 0.1, n_clients)  # 10% de défaut
})

# Sauvegarde dans data/raw/
df.to_csv("data/raw/clients_bancaires_5000.csv", index=False)
print("✅ CSV généré : data/raw/clients_bancaires_5000.csv")