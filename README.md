Protein Function Prediction Web App

🔬 Overview
This Streamlit web application predicts whether a given protein sequence is an Enzyme or Non-Enzyme based on its amino acid composition. The prediction is powered by a pre-trained Random Forest model.

Features

Input a protein sequence in plain text format.

Extracts amino acid composition features using BioPython.

Predicts protein function (Enzyme vs Non-Enzyme) using a Random Forest model.

User-friendly interface built with Streamlit.

Requirements

Python ≥ 3.8

Streamlit

Biopython

pandas

scikit-learn

joblib

Install dependencies using:

pip install streamlit biopython pandas scikit-learn joblib

Usage

Clone the repository:

git clone https://github.com/yourusername/protein-function-prediction.git
cd protein-function-prediction


Make sure the trained model rf_model.pkl is in the same folder.

Run the Streamlit app:

streamlit run app.py


Paste your protein sequence into the text area and click Predict.

✅ Enzyme → predicted as enzyme

❌ Non-Enzyme → predicted as non-enzyme

How It Works

Feature Extraction: Uses BioPython’s ProteinAnalysis to calculate amino acid composition.

Prediction: A Random Forest model (rf_model.pkl) classifies the sequence as enzyme (1) or non-enzyme (0).

Output: Displays a clear prediction with a success or warning message.

File Structure
protein-function-prediction/
│
├── app.py          # Streamlit application script
├── rf_model.pkl    # Pre-trained Random Forest model
├── README.md       # Project description
└── requirements.txt # Optional: pip dependencies

License

Specify your license here (e.g., MIT License).
