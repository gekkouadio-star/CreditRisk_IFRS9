# CreditRisk_IFRS9 – Modèle de Scoring Crédit & Calcul ECL (IFRS 9)

## Présentation du projet

Ce projet a pour objectif de construire un **pipeline complet d’analyse du risque de crédit** conforme aux exigences de la norme **IFRS 9**.

Il permet de :
- nettoyer des données clients bancaires,
- construire un **modèle de scoring crédit (PD)**,
- estimer les paramètres **LGD** et **EAD**,
- calculer la **perte attendue (ECL)**,
- classifier les clients en **Stage IFRS 9 (Stage 1 / Stage 2 / Stage 3)**,
- afficher un **dashboard interactif Streamlit**.

---

## Objectifs principaux

✔ Construire un modèle de **Probabilité de Défaut (PD)**  
✔ Estimer **LGD** (Loss Given Default) et **EAD** (Exposure At Default)  
✔ Calculer la **Expected Credit Loss (ECL)**  
✔ Appliquer la logique IFRS9 pour classer les expositions en **Stage 1, Stage 2, Stage 3**  
✔ Générer des graphiques et un tableau de bord interactif

---

## IFRS 9 : Définition et utilité en banque

La norme **IFRS 9** signifie **International Financial Reporting Standard 9**.

IFRS9 a été introduite pour **améliorer la transparence et la précision des pertes de crédit attendues** sur les prêts et autres actifs financiers.  
Elle remplace l’ancienne norme **IAS 39**.

IFRS9 impose aux banques de **provisionner les pertes attendues avant même qu’un défaut ne survienne**, ce qui renforce la gestion proactive du risque.

---

## Concepts clés IFRS 9

### 🟢 Stage 1
Clients ou prêts **sans détérioration significative du risque de crédit depuis l’octroi**.  
➡ Provision : **pertes attendues sur 12 mois** (ECL sur 1 an).

### 🟠 Stage 2
Clients ou prêts **avec risque de crédit détérioré mais pas en défaut**.  
➡ Provision : **pertes attendues sur toute la durée restante du prêt**.

### 🔴 Stage 3
Clients ou prêts **en défaut**.  
➡ Provision : **pertes attendues sur toute la durée**, avec traitement comptable plus strict.

---

## Paramètres de risque utilisés

### PD (Probability of Default)
➡ Probabilité qu’un client **ne rembourse pas** son crédit.

### LGD (Loss Given Default)
➡ Pourcentage de perte subie par la banque **en cas de défaut**.

### EAD (Exposure at Default)
➡ Montant exposé au moment du défaut (capital restant dû + exposition).

### ECL (Expected Credit Loss)
➡ Perte attendue calculée comme :

\[
ECL = PD \times LGD \times EAD
\]

---

## Résumé IFRS9

En résumé : **IFRS9 sert à prévoir et comptabiliser les pertes sur les prêts avant qu’elles ne se produisent réellement**, en les classant selon le risque du client (**Stage 1, Stage 2 ou Stage 3**).

---

## Structure du projet

```bash
CreditRisk_IFRS9/
│
├─ data/
│   ├─ raw/             # CSV bruts
│   └─ processed/       # Données nettoyées et enrichies
│
├─ scripts/
│   ├─ 01_data_preprocessing.py
│   ├─ 02_feature_engineering.py
│   ├─ 03_scoring_model.py
│   ├─ 04_LGD_EAD.py
│   ├─ 05_IFRS9_classification.py
│   ├─ 06_dashboard.py
│   └─ 07_dashboard_streamlit.py
│
├─ reports/
│   └─ figures/
│
├─ requirements.txt
└─ README.md