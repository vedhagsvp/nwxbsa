import pandas as pd

def run_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    # Example cleaning logic
    df = df.dropna()
    df.columns = [c.lower() for c in df.columns]
    
    return df
