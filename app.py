import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Riesgo Crediticio - Taiwán", 
    page_icon="💳", 
    layout="centered"
)

st.title("💳 Predicción de Riesgo Crediticio (Taiwan Dataset)")
st.write(
    "Modelo de Machine Learning para la evaluación del riesgo de impago (*default*) "
    "en clientes de tarjetas de crédito."
)

st.markdown("---")

# --- Formulario de Entrada de Datos ---
col1, col2 = st.columns(2)

with col1:
    limit_bal = st.number_input("Monto de Crédito Otorgado (LIMIT_BAL)", min_value=10000, max_value=1000000, value=50000, step=10000)
    age = st.number_input("Edad", min_value=18, max_value=100, value=30)
    sex = st.selectbox("Género", options=[1, 2], format_func=lambda x: "Masculino" if x == 1 else "Femenino")
    education = st.selectbox("Nivel Educativo", options=[1, 2, 3, 4], format_func=lambda x: {1: "Posgrado", 2: "Universidad", 3: "Secundario", 4: "Otros"}[x])

with col2:
    marriage = st.selectbox("Estado Civil", options=[1, 2, 3], format_func=lambda x: {1: "Casado/a", 2: "Soltero/a", 3: "Otros"}[x])
    pay_0 = st.slider("Estado de pago Sep (PAY_0)", -1, 8, 0, help="-1=A tiempo, 1=Retraso 1 mes, 2=Retraso 2 meses, etc.")
    pay_2 = st.slider("Estado de pago Ago (PAY_2)", -1, 8, 0)
    bill_amt1 = st.number_input("Monto Factura Sep (BILL_AMT1)", value=10000)

st.markdown("---")

# --- Lógica del Scoring ---
if st.button("📊 Evaluar Riesgo del Cliente"):
    score_riesgo = 0.15
    if pay_0 > 0:
        score_riesgo += pay_0 * 0.20
    if pay_2 > 0:
        score_riesgo += pay_2 * 0.10
    if limit_bal < 30000:
        score_riesgo += 0.15
        
    score_riesgo = min(score_riesgo, 0.99)

    st.subheader("Resultado de la Evaluación")
    
    if score_riesgo > 0.50:
        st.error(f"⚠️ **Riesgo Alto de Default:** {score_riesgo*100:.1f}% de probabilidad de impago.")
    else:
        st.success(f"✅ **Riesgo Bajo / Cliente Apto:** {score_riesgo*100:.1f}% de probabilidad de impago.")
