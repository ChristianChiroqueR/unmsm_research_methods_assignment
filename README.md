# UNMSM Research Methods & Scientific Integrity in AI
## Doctoral Program in Deep Technologies

**Student:** Christian Chiroque Ruiz  

**Instructor:** Dr. Loveleen Gaur  

## Project Overview

This repository contains all deliverables for the 16-session capstone project of the Research Methods & Scientific Integrity in AI course. The project follows a single research thread: designing, implementing, and evaluating a Graph Machine Learning artifact for Anti-Money Laundering detection in fintech transaction networks.

**Research Question:**  
How can a graph machine learning artifact be designed, implemented, and evaluated to improve the detection of money laundering networks in fintech transaction graphs, under conditions of class imbalance and limited labelled data — with design requirements derived from the operational context of financial intelligence units?

## Repository Structure

├── 01_paradigm/          # Paradigm justification statement
├── 02_method/            # Method-fit matrix and selection
├── 03_protocol/          # Research protocol (v0.1 → v2.0)
├── 04_literature/        # Systematic review, PRISMA diagram, gap analysis
├── 05_pipeline/          # Reproducible ML pipeline (Session 5)
│   ├── notebook.ipynb    # End-user notebook
│   └── src/train.py      # Training script
├── 06_repro_audit/       # Reproducibility audit of a published paper

---

## Reproducible Pipeline (Session 5)

**Dataset:** Elliptic Bitcoin Dataset — 203,769 transactions, 166 features

**Model:** Logistic Regression classifier  

### Reproduce this project

**1. Clone the repository**
```bash
git clone https://github.com/ChristianChiroqueR/unmsm_research_methods_assignment.git
cd unmsm_research_methods_assignment
```

**2. Pull the data**
```bash
dvc pull
```

**3. Option A — Run with Docker**
```bash
docker build -t unmsm-project .
docker run -it --rm -v "$(pwd):/project" unmsm-project
python 05_pipeline/src/train.py --seed 42
```

**4. Option B — Run locally**
```bash
pip install -r requirements.txt
python 05_pipeline/src/train.py --seed 42
```

---

## Reproducibility Checklist

- ✅ Seeds set for Python, NumPy
- ✅ Train/test split BEFORE preprocessing (no data leakage)
- ✅ MLflow tracks all parameters, metrics and artifacts
- ✅ Dataset versioned with DVC
- ✅ Environment frozen in Dockerfile + pinned requirements.txt
- ✅ Meaningful commit history throughout the course

## Dataset

The Elliptic Bitcoin Dataset is tracked via DVC and stored in Google Drive — not directly in this repository. To access it:

```bash
dvc pull
```

Source: [Elliptic Data Set — Kaggle](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set)  


