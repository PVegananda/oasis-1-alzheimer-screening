---
title: OASIS-1 Dementia Risk Screening
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: "5.0.0"
python_version: "3.10"
app_file: app.py
pinned: true
license: mit
short_description: Machine learning screening application for dementia risk using OASIS-1 clinical data
---

<p align="center">
  <a href="https://github.com/PVegananda/oasis-1-dementia-risk-screening">
    <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="180" alt="OASIS-1 Dementia Risk Screening">
  </a>
</p>

<h1 align="center">OASIS-1 Dementia Risk Screening</h1>

<p align="center">
  Machine learning screening application for dementia risk using clinical data from the OASIS-1 dataset.
</p>

<p align="center">
  <a href="https://github.com/PVegananda/oasis-1-dementia-risk-screening"><img src="https://img.shields.io/github/repo-size/PVegananda/oasis-1-dementia-risk-screening?label=Repository%20size" alt="Repository size"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python 3.10"></a>
  <a href="https://www.gradio.app/"><img src="https://img.shields.io/badge/Gradio-5.0-FF7C00?logo=gradio&logoColor=white" alt="Gradio 5.0"></a>
  <a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-1.8-F7931E?logo=scikit-learn&logoColor=white" alt="scikit-learn 1.8"></a>
  <a href="https://huggingface.co/"><img src="https://img.shields.io/badge/Deployment-Hugging%20Face-FFD21E?logo=huggingface&logoColor=black" alt="Hugging Face deployment"></a>
  <img src="https://img.shields.io/badge/License-MIT-111827" alt="MIT License">
</p>

An educational machine learning application for screening dementia risk from clinical data in the OASIS-1 dataset. The application provides an interactive Gradio interface and compares predictions from three classification models: K-Nearest Neighbors, Decision Tree, and Gaussian Naive Bayes.

> This project is intended for academic, research, and portfolio purposes. It is not a medical diagnostic tool and must not replace an assessment by a qualified healthcare professional.

## Project Overview

The application accepts selected demographic, cognitive, and brain-volume features, scales the input data, and returns a prediction with the selected model's confidence, accuracy, and F1-score.

The project demonstrates an end-to-end machine learning workflow:

1. Preparing clinical features from the OASIS-1 dataset.
2. Scaling input data consistently with the training pipeline.
3. Training and evaluating multiple classification algorithms.
4. Persisting trained models with Joblib.
5. Serving predictions through a lightweight Gradio web interface.

## Technology Stack

| Category | Technology |
| --- | --- |
| Language | Python 3.10 |
| User interface | Gradio 5.0 |
| Machine learning | scikit-learn 1.8 |
| Numerical computing | NumPy 1.26 |
| Model persistence | Joblib |
| Dataset | OASIS-1 Cross-Sectional |
| Deployment target | Hugging Face Spaces |

## Model Performance

| Model | Accuracy | F1-score |
| --- | ---: | ---: |
| K-Nearest Neighbors (k=5, Euclidean) | 95.45% | 95.43% |
| Decision Tree (Gini) | 100.00% | 100.00% |
| Gaussian Naive Bayes | 100.00% | 100.00% |

These metrics reflect the evaluation performed for this academic project. They should not be interpreted as clinical performance or as evidence of diagnostic accuracy in real-world settings.

## Input Features

| Feature | Description | Expected range or format |
| --- | --- | --- |
| Gender | Patient gender | Male / Female |
| Age | Patient age | 55–98 years |
| EDUC | Education level | 1–5 |
| SES | Socioeconomic status | 1–5 |
| MMSE | Mini-Mental State Examination score | 0–30 |
| CDR | Clinical Dementia Rating | 0 / 0.5 / 1 / 2 |
| eTIV | Estimated total intracranial volume | Approximately 900–2,000 cc |
| nWBV | Normalized whole brain volume | Approximately 0.60–0.90 |

## Running Locally

### Requirements

- Python 3.10 or compatible
- pip

### Installation

```bash
git clone https://github.com/PVegananda/oasis-1-dementia-risk-screening.git
cd oasis-1-dementia-risk-screening
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### Launch the application

```bash
python app.py
```

Open the local Gradio URL shown in the terminal, then enter the clinical features and select a model to generate a screening result.

## Repository Structure

| File | Description |
| --- | --- |
| `app.py` | Gradio interface and prediction workflow |
| `UTS_ML_OASIS1_Complete.ipynb` | Data preparation, training, and evaluation notebook |
| `scaler.joblib` | Fitted feature scaler |
| `*_model.joblib` | Persisted KNN, Decision Tree, and Naive Bayes models |
| `metadata.json` | Model evaluation metrics used by the interface |
| `requirements.txt` | Python dependencies |

## Dataset and References

This project uses the OASIS-1 Cross-Sectional dataset from the Open Access Series of Imaging Studies.

- Dataset source: [OASIS-1](https://sites.wustl.edu/oasisbrains/home/oasis-1/)
- Marcus, D. S., et al. (2007). OASIS: Cross-sectional MRI data in young, middle aged, nondemented, and demented older adults. *Journal of Cognitive Neuroscience*, 19(9), 1498–1507.
- Cabanillas-Carbonell, M., & Zapata-Paulini, J. (2025). Evaluation of machine learning methods for Alzheimer's disease. *Brain, Behavior, & Immunity - Integrative*, 100957.
- Lazli, L. (2025). Improved Alzheimer's disease diagnosis with machine learning. *JMIRx Med*, 6, e60866.
- Sarica, A., et al. (2023). Machine learning approaches for Alzheimer's disease neuroimaging. *Frontiers in Aging Neuroscience*.

## Academic Context

This project was developed as part of the Machine Learning Midterm Project at Universitas Dian Nuswantoro, academic year 2025/2026.

- Lecturer: Junta Zeniarja, M.Kom

## Disclaimer

The predictions generated by this application are statistical outputs from machine learning models trained on a research dataset. They are not medical advice, a diagnosis, or a substitute for consultation with a neurologist or other qualified healthcare professional.
