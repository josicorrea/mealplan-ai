import streamlit as st
import requests

st.title("Plan de Alimentación Personalizado con IA")

preferencias = st.text_input("Preferencias alimenticias", "vegetariano, sin gluten")
dias = st.number_input("Cantidad de días", min_value=1, max_value=14, value=3)

if st.button("Generar plan"):
    with st.spinner("Generando plan..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/generar-mealplan",
                json={"preferencias": preferencias, "dias": dias},
                timeout=60
            )
            response.raise_for_status()
            plan = response.json().get("plan", "No se recibió plan.")
            st.success("Plan generado:")
            st.text_area("Plan de alimentación", plan, height=400)
        except Exception as e:
            st.error(f"Error: {e}")
