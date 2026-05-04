import gradio as gr
import numpy as np
import joblib
import json
import os
import warnings

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.abspath(__file__))

try:
    scaler = joblib.load(os.path.join(BASE, "scaler.joblib"))
    knn = joblib.load(os.path.join(BASE, "knn_model.joblib"))
    dt = joblib.load(os.path.join(BASE, "dt_model.joblib"))
    nb = joblib.load(os.path.join(BASE, "nb_model.joblib"))
    
    with open(os.path.join(BASE, "metadata.json")) as f:
        meta = json.load(f)
    
    models_loaded = True
except Exception as e:
    models_loaded = False
    error_msg = str(e)

def predict_fn(gender, age, educ, ses, mmse, cdr, etiv, nwbv, model_name):
    if not models_loaded:
        return f"Error loading models: {error_msg}"
    
    try:
        gender_val = 1 if gender.strip().lower() == "female" else 0
        age_val = float(age)
        educ_val = float(educ)
        ses_val = float(ses)
        mmse_val = float(mmse)
        cdr_val = float(cdr)
        etiv_val = float(etiv)
        nwbv_val = float(nwbv)
        
        X = np.array([[gender_val, age_val, educ_val, ses_val, mmse_val, cdr_val, etiv_val, nwbv_val]])
        X_scaled = scaler.transform(X)
        
        model_dict = {"KNN": knn, "Decision Tree": dt, "Naive Bayes": nb}
        selected_model = model_dict.get(model_name.strip(), knn)
        
        prediction = int(selected_model.predict(X_scaled)[0])
        prob = selected_model.predict_proba(X_scaled)[0] if hasattr(selected_model, "predict_proba") else None
        
        result = "DEMENTED" if prediction == 1 else "NONDEMENTED"
        confidence = (max(prob) * 100) if prob is not None else 0
        
        acc_key = f"{model_name.strip()}_acc"
        f1_key = f"{model_name.strip()}_f1"
        
        if model_name.strip() == "KNN":
            accuracy = meta.get("knn_acc", 0) * 100
            f1 = meta.get("knn_f1", 0) * 100
        elif model_name.strip() == "Decision Tree":
            accuracy = meta.get("dt_acc", 0) * 100
            f1 = meta.get("dt_f1", 0) * 100
        else:
            accuracy = meta.get("nb_acc", 0) * 100
            f1 = meta.get("nb_f1", 0) * 100
        
        output = f"Diagnosis: {result}\nConfidence: {confidence:.1f}%\nModel Accuracy: {accuracy:.2f}%\nF1-Score: {f1:.2f}%"
        return output
        
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="OASIS-1 Alzheimer") as app:
    gr.HTML("<h1>OASIS-1 Alzheimer Detection</h1>")
    gr.HTML("<p>Early dementia detection from clinical data</p>")
    
    with gr.Row():
        gender = gr.Textbox(value="Male", label="Gender")
        age = gr.Textbox(value="72", label="Age")
    
    with gr.Row():
        educ = gr.Textbox(value="3", label="Education")
        ses = gr.Textbox(value="2", label="SES")
    
    with gr.Row():
        mmse = gr.Textbox(value="27", label="MMSE")
        cdr = gr.Textbox(value="0", label="CDR")
    
    with gr.Row():
        etiv = gr.Textbox(value="1450", label="eTIV")
        nwbv = gr.Textbox(value="0.74", label="nWBV")
    
    model = gr.Textbox(value="KNN", label="Model: KNN|Decision Tree|Naive Bayes")
    
    with gr.Row():
        submit_btn = gr.Button("Predict")
        output = gr.Textbox(label="Result")
    
    submit_btn.click(
        fn=predict_fn,
        inputs=[gender, age, educ, ses, mmse, cdr, etiv, nwbv, model],
        outputs=output
    )

if __name__ == "__main__":
    app.launch()




