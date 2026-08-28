import pandas as pd
import streamlit as st
import httpx

BASE_URL = "http://localhost:8000"

def main():
    st.title("FastlyDep eClipseBord")
    st.divider()
    st.markdown("### Solar Eclipse Data ")

# Gör try / except för att hantera fel ifall backend inte funkar etc.
    try:
        kpis_response = httpx.get(f"{BASE_URL}/eclipses/kpi")
        kpis = kpis_response.json()
        # Eftersom jag har 3 KPIer så skapar jag 3 kolumner för dom att va i.
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Total Eclipses", value=kpis.get("total_eclipses", 0))
        with col2:
            st.metric(label="Max Magnitude", value=round(kpis.get("max_magnitude", 0), 3))
        with col3:
            st.metric(label="Max Gamma", value=round(kpis.get("max_gamma", 2), 3))

        # Dra en linje över sidan
        st.divider()

        st.subheader("Eclipse Data")
        table_response = httpx.get(f"{BASE_URL}/eclipses")
        table_data = table_response.json()

        st.dataframe(table_data)

    except Exception as e:
        st.error(f"Error, cant connect to backend: {e}")

if __name__ == "__main__":
    main()


