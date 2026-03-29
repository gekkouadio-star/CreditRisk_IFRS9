import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1️⃣ Charger les données
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/clients_IFRS9.csv")
    
    # Générer des colonnes manquantes si nécessaire
    if 'LGD' not in df.columns:
        np.random.seed(42)
        df['LGD'] = np.random.uniform(0.3, 0.7, size=len(df))
    if 'EAD' not in df.columns:
        df['EAD'] = df['encours_total']
    if 'PD' not in df.columns:
        df['PD'] = np.random.uniform(0, 0.2, size=len(df))
    if 'ECL' not in df.columns:
        df['ECL'] = df['PD'] * df['LGD'] * df['EAD']
    if 'taux_endettement' not in df.columns:
        df['taux_endettement'] = df['encours_total'] / df['revenu_mensuel'] / 12
    return df

df = load_data()

# -----------------------------
# 2️⃣ Sidebar navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Aller à :", 
    ["Aperçu des données", "KPIs par Stage", "Histogrammes interactifs", "Répartition Stage IFRS9"]
)

# -----------------------------
# 3️⃣ Filtres globaux
# -----------------------------
st.sidebar.title("Filtres")
stage_filter = st.sidebar.multiselect(
    "Sélectionner Stage(s)", options=sorted(df['Stage_IFRS9'].unique()), default=sorted(df['Stage_IFRS9'].unique())
)
anciennete_filter = st.sidebar.slider(
    "Ancienneté du client (années)",
    int(df['anciennete_client'].min()),
    int(df['anciennete_client'].max()),
    (int(df['anciennete_client'].min()), int(df['anciennete_client'].max()))
)
taux_endettement_filter = st.sidebar.slider(
    "Taux d'endettement (%)",
    int(df['taux_endettement'].min()*100),
    int(df['taux_endettement'].max()*100),
    (int(df['taux_endettement'].min()*100), int(df['taux_endettement'].max()*100))
)

# Appliquer les filtres
filtered_df = df[
    (df['Stage_IFRS9'].isin(stage_filter)) &
    (df['anciennete_client'] >= anciennete_filter[0]) &
    (df['anciennete_client'] <= anciennete_filter[1]) &
    (df['taux_endettement']*100 >= taux_endettement_filter[0]) &
    (df['taux_endettement']*100 <= taux_endettement_filter[1])
]

# -----------------------------
# 4️⃣ Pages avec explications
# -----------------------------
if page == "Aperçu des données":
    st.title("Aperçu des données")
    st.markdown("""
    Cette page montre un extrait des clients filtrés selon vos critères.
    
    - `client_id` : Identifiant unique du client
    - `revenu_mensuel` : Revenu mensuel du client
    - `encours_total` : Total des crédits en cours
    - `anciennete_client` : Ancienneté du client en années
    - `Stage_IFRS9` : Stage IFRS9 (1 = pas détérioré, 2 = risque détérioré, 3 = défaut)
    - `PD` : Probabilité de défaut
    - `EAD` : Exposition au défaut
    - `LGD` : Perte en cas de défaut
    - `ECL` : Perte attendue
    """)
    st.dataframe(filtered_df.head(20))

elif page == "KPIs par Stage":
    st.title("KPIs par Stage IFRS9")
    st.markdown("""
    Cette page calcule les principaux indicateurs par Stage IFRS9 :
    - **Total ECL** : Somme des pertes attendues par Stage
    - **Moyenne PD** : Probabilité moyenne de défaut par Stage
    - **Nombre de clients** : Nombre de clients par Stage
    """)
    kpis = filtered_df.groupby('Stage_IFRS9').agg(
        Total_ECL=('ECL','sum'),
        Moyenne_PD=('PD','mean'),
        Nombre_Clients=('PD','count')
    ).reset_index()
    st.dataframe(kpis)
    
    st.subheader("Total ECL par Stage")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x='Stage_IFRS9', y='Total_ECL', data=kpis, palette=['green','orange','red'], ax=ax)
    ax.set_ylabel("Total ECL")
    ax.set_xlabel("Stage IFRS9")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    
    st.subheader("Moyenne PD par Stage")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x='Stage_IFRS9', y='Moyenne_PD', data=kpis, palette=['green','orange','red'], ax=ax)
    ax.set_ylabel("PD moyenne")
    ax.set_xlabel("Stage IFRS9")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

elif page == "Histogrammes interactifs":
    st.title("Histogrammes PD/ECL")
    st.markdown("""
    Les histogrammes permettent de visualiser la distribution des probabilités de défaut (PD) 
    et des pertes attendues (ECL) sur les clients filtrés.
    """)
    
    st.subheader("Distribution PD")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(filtered_df['PD'], bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_xlabel("PD")
    ax.set_ylabel("Nombre de clients")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    
    st.subheader("Distribution ECL")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(filtered_df['ECL'], bins=30, color='salmon', ax=ax)
    ax.set_xlabel("ECL")
    ax.set_ylabel("Nombre de clients")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

elif page == "Répartition Stage IFRS9":
    st.title("🟢🟠🔴 Répartition Stage IFRS9")
    st.markdown("""
    Ce graphique montre la proportion de clients dans chaque Stage IFRS9 :
    - **Stage 1 (vert)** : Clients sans détérioration significative
    - **Stage 2 (orange)** : Clients avec risque détérioré
    - **Stage 3 (rouge)** : Clients en défaut
    """)
    stage_counts = filtered_df['Stage_IFRS9'].value_counts().sort_index()
    fig, ax = plt.subplots()
    stage_counts.plot.pie(autopct="%1.1f%%", colors=['green','orange','red'], ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)