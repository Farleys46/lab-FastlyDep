import pandas as pd
from backend.constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "solar.csv")

df = df.fillna({
    "Path Width (km)": 0, 
    "Central Duration": "missing"
})

def get_kpis():
    return {
        "total_eclipses": len(df),
        "max_magnitude": float(df['Eclipse Magnitude'].max()),
        "max_gamma": float(df['Gamma'].max())
    }