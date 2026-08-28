from fastapi import FastAPI
from backend.data_processing import df, get_kpis

app = FastAPI()

@app.get("/eclipses")
async def show_data(limit: int = 100):
    # Pga min temporära "skit laptop" med 4gb Ram
    # Så behöver jag sätta en gräns på anrop eftersom de 11000 raderna kunde inte laddas in i Swagger UI
    # när jag kör "execute" Detta är en workaround för att kunna visa data i Swagger UI.
    return df.head(limit).to_dict(orient="records")

@app.get("/eclipses/kpi")
async def get_eclipse_kpis():
    return get_kpis()
