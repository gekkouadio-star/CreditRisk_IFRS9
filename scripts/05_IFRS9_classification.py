import pandas as pd

def classify_ifrs9(input_file, output_file="data/processed/clients_IFRS9.csv"):
    """
    Classifie les clients en Stage 1, 2 et 3 selon IFRS9.
    - Stage 1 : PD < 2%
    - Stage 2 : 2% <= PD < 10%
    - Stage 3 : PD >= 10%
    """
    
    df = pd.read_csv(input_file)
    
    def get_stage(row):
        if row['PD'] >= 0.10:
            return 3
        elif row['PD'] >= 0.02:
            return 2
        else:
            return 1
    
    df['Stage_IFRS9'] = df.apply(get_stage, axis=1)
    
    df.to_csv(output_file, index=False)
    print(f"✅ Classification IFRS9 terminée. Fichier sauvegardé : {output_file}")
    return df

if __name__ == "__main__":
    classify_ifrs9("data/processed/clients_clean.csv")