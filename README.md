---
title: OASIS-1 Alzheimer Detection System
emoji: 🧠
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: "5.0.0"
python_version: "3.10"
app_file: app.py
pinned: true
license: mit
short_description: Deteksi dini demensia Alzheimer berbasis data klinis OASIS-1
---

# 🧠 OASIS-1 Alzheimer Detection System

Sistem deteksi dini demensia Alzheimer berbasis **machine learning** menggunakan dataset klinis OASIS-1 dari **Washington University School of Medicine + Harvard University + NIH**.

## 📌 Deskripsi

Aplikasi ini memungkinkan pengguna memasukkan data klinis pasien secara manual dan mendapatkan prediksi status demensia (**Demented** atau **Nondemented**) menggunakan tiga algoritma klasifikasi.

## 🤖 Algoritma yang Digunakan

| Model | Accuracy | F1-Score |
|-------|----------|----------|
| KNN (k=5, Euclidean) | 95.45% | 95.43% |
| Decision Tree (Gini) | 100.00% | 100.00% |
| Naive Bayes (Gaussian) | 100.00% | 100.00% |

## 📊 Dataset

**OASIS-1 Cross-Sectional** (Open Access Series of Imaging Studies)

- **Sumber resmi:** https://sites.wustl.edu/oasisbrains/home/oasis-1/
- **Institusi:** Washington University + Harvard University + NIH
- **Subjek:** 436 individu usia 60–96 tahun
- **Referensi:** Marcus, D. S., et al. (2007). *Journal of Cognitive Neuroscience*, 19(9), 1498–1507.

## 🏥 Fitur Input

| Fitur | Keterangan | Rentang |
|-------|-----------|---------|
| Gender | Jenis kelamin | Male / Female |
| Age | Usia | 55–98 tahun |
| EDUC | Tingkat pendidikan | 1 (SD) – 5 (S2+) |
| SES | Status sosial ekonomi | 1 (tinggi) – 5 (rendah) |
| MMSE | Mini Mental State Examination | 0–30 (27+ normal) |
| CDR | Clinical Dementia Rating | 0 / 0.5 / 1 / 2 |
| eTIV | Estimated Total Intracranial Volume | ~900–2000 cc |
| nWBV | Normalized Whole Brain Volume | 0.60–0.90 |

## ⚠️ Disclaimer

Aplikasi ini adalah **alat skrining akademis** berbasis ML untuk keperluan penelitian dan edukasi. **Bukan pengganti diagnosis medis profesional.** Konsultasikan hasil dengan dokter spesialis neurologi.

## 📚 Referensi Ilmiah

1. Marcus, D. S., et al. (2007). OASIS: Cross-sectional MRI Data. *J. Cognitive Neuroscience*, 19(9).
2. Cabanillas-Carbonell & Zapata-Paulini (2025). Evaluation of ML for Alzheimer's. *Brain, Behavior and Immunity Integrative*. DOI: 10.1016/j.bbih.2025.100957
3. Lazli, L. (2025). Improved Alzheimer Diagnosis with ML. *JMIRx Med*, 6:e60866.
4. Sarica et al. (2023). Random Forest for Alzheimer's Neuroimaging. *Frontiers in Aging Neuroscience*.

## 🎓 Proyek

**UTS Pembelajaran Mesin — Universitas Dian Nuswantoro 2025/2026**
Dosen: Junta Zeniarja, M.Kom
