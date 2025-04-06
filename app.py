import streamlit as st
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import joblib

model = joblib.load("rf_model.pkl")

def extract_features(seq):
    analysis = ProteinAnalysis(seq)
    aa_comp = analysis.get_amino_acids_percent()
    return pd.DataFrame([aa_comp])

st.title("🔬 Protein Function Prediction")
st.markdown("🧬 Predict whether your protein is an **Enzyme** or **Non-Enzyme** based on its amino acid composition.")

sequence = st.text_area("Paste your protein sequence:", height=100)

if st.button("Predict"):
    if sequence:
        try:
            features = extract_features(sequence)
            pred = model.predict(features)[0]
            result = "✅ Enzyme" if pred == 1 else "❌ Non-Enzyme"
            st.success(f"Prediction: **{result}**")
        except Exception as e:
            st.error(f"Error processing sequence: {e}")
    else:
        st.warning("Please enter a sequence.")
