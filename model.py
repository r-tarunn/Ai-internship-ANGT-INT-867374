import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(file_path):
   
    df = pd.read_csv(file_path)

    df_numeric = df.select_dtypes(include=['float64', 'int64'])

    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(df_numeric)

    df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

    anomalies = df[df['anomaly'] == 1]

    return df, anomalies