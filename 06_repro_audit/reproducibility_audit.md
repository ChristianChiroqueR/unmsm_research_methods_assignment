# Reproducibility Audit — Mohawesh et al. (2026)

## Paper source

Mohawesh, R., Maqsood, S., Bany Salameh, H., & Elrefae, G. (2026). Leveraging GraphSAGE and
large language models with cross-attention for transaction fraud detection: Evidence from credit
card and PaySim datasets. *Information Processing and Management, 63*, 104860.
https://doi.org/10.1016/j.ipm.2026.104860

**Audit date:** 2026-08-01  
**Reason for selection:** This paper is a direct methodological comparator for this project.
It applies GraphSAGE to financial fraud detection on the Elliptic Bitcoin dataset (among others),
which is the same dataset used in this thesis pipeline. Auditing it makes the reproducibility
assessment substantively relevant rather than decorative.

---

## Audit boundary

This assessment examines the reporting and access conditions of Mohawesh et al. (2026) based
on the published article and its linked materials as available on the audit date. It does not
claim to have reproduced the reported results (89.1% accuracy on ECCD, 90.0% on PaySim).
A missing item means only that the information was not locatable in the checked record — it
is not proof of an error in the underlying findings.

---

## Criterion-by-criterion assessment

| Criterion | Assessment | Evidence observed | Practical consequence |
|---|---|---|---|
| **Data access** | Public | ECCD (Kaggle), PaySim (GitHub/Kaggle), and Elliptic (Kaggle) are all freely downloadable without permission requests. | A qualified researcher can retrieve all three datasets immediately. |
| **Code availability** | Not public | The data availability statement reads: "The authors do not have permission to share data." No public repository is linked in the article. | The exact preprocessing pipeline, graph construction logic, and training loop cannot be independently inspected. |
| **Random seeds** | Partial | The paper states results are "averaged over five random seeds" and reports ±SD and 95% CI (Table 3). The exact seed values are not reported anywhere in the article. | Five-run averaging is a good practice, but exact reruns producing identical per-run results are not possible without the seed values. |
| **Partitions and leakage controls** | Partial | A chronological 70/10/20 train/validation/test split is documented and justified as a leakage control measure. The ECCD graph construction (k-NN with k=10, 10D PCA, cosine similarity) is described. However, the full executable preprocessing pipeline is unavailable without the code. | The split strategy is sound and documented; exact partition boundaries and fit order for transformations cannot be verified independently. |
| **Repetitions and stability** | Reported | Results in Table 3 are averaged over five runs with both standard deviations (±SD) and 95% confidence intervals. A paired t-test (Table 5) is used to confirm statistical significance (p=0.012 on ECCD, p=0.008 on PaySim). | This is above-average reporting for the field. Uncertainty is quantified and statistical claims are testable in principle. |
| **Evaluation and uncertainty** | Reported | Five metrics are used: Accuracy, Precision, Recall, F1-score, AUC. Additional metrics include G-Mean and MCC (Table 6), an ablation study (Table 7), a cost-sensitive analysis (Table 10), and a GNNExplainer interpretability analysis. | Comprehensive metric coverage. The cost-sensitive framing (FN:FP cost ratio of 100:1) is especially relevant for fraud detection contexts. |
| **Compute and environment** | Partial | Hardware is described (Google Colab Pro, dual-core vCPU, NVIDIA Tesla T4 16 GB VRAM, ~25 GB RAM). Library versions are named (PyTorch 2.1, HuggingFace Transformers). No requirements.txt, conda environment file, Dockerfile, or container image is provided. | Runtime can be approximated but exact numerical reproduction across environments is not guaranteed without a pinned environment specification. |

---

## Transparent score

Each criterion is scored 0–2: 0 = no public evidence located; 1 = partial reporting or
conditional access; 2 = publicly executable record.

| Criterion | Score | Reason |
|---|---|---|
| Data access | 2/2 | All three datasets are freely and immediately downloadable. |
| Code availability | 0/2 | No public implementation located. |
| Random seeds | 1/2 | Five-run averaging with SD/CI reported; exact seed values absent. |
| Partitions and leakage controls | 1/2 | Split strategy documented; full executable pipeline unavailable. |
| Repetitions and stability | 2/2 | SD, CI, and paired t-tests reported across all main results. |
| Evaluation and uncertainty | 2/2 | Five primary metrics plus G-Mean, MCC, ablation, cost-sensitivity, and explainability. |
| Compute and environment | 1/2 | Hardware and library versions named; no pinned environment file provided. |

**Total: 9/14 (64%) — moderate public reproducibility.**

This score is a reading aid, not a judgment of author intent or scientific validity. A paper
can be methodologically sound and practically useful while being partially difficult to reproduce,
and a higher score would not prove that its performance claims are correct in other settings.

---

## Overall reading

Mohawesh et al. (2026) is one of the more carefully reported papers in the GNN fraud detection
space. The use of five-seed averaging, confidence intervals, paired t-tests, and an ablation
study reflects a genuine effort to make claims defensible. The datasets are publicly accessible,
which removes one of the most common barriers to independent verification.

The main reproducibility gap is the absence of released code. Without it, the graph construction
procedure for ECCD (which uses engineered semantic descriptors derived from PCA-transformed
features — an inherently ambiguous mapping), the exact SMOTE oversampling implementation, and
the DistilBERT tokenization choices cannot be independently verified. The missing seed values
are a secondary gap: five-run averaging reduces but does not eliminate run-to-run variance.

The paper's handling of dataset limitations is notably honest: the authors explicitly state
that ECCD (2013) and PaySim (pre-2016) may not reflect 2026 fraud behavior, and they include
an additional Elliptic experiment as out-of-sample temporal evidence. This kind of epistemic
honesty about scope is worth noting as good practice.

---

## What this repository does differently

This project addresses several of the gaps identified above:

| Gap in audited paper | Practice in this repository |
|---|---|
| Seed values not reported | Seeds are fixed and logged explicitly in MLflow parameters (`seed=42`, plus reproducibility seeds across runs) |
| No public code | Full pipeline committed to GitHub under open license |
| No environment specification | `requirements.txt` with pinned versions committed; Dockerfile provided |
| Preprocessing pipeline not inspectable | DVC tracks data versioning; notebook cells document each transformation step in order |
| No leakage documentation | Train-only preprocessing enforced; fit/transform separation documented in notebook comments |

These practices make the workflow easier to inspect and rerun. They do not make the exploratory
GNN model operationally validated or eliminate the need for independent replication on held-out
data.
