# Protocol v0.1

**Student:** Christian Chiroque Ruiz  

**Instructor:** Dr. Loveleen Gaur  

**Date:** June 2026

## 01 Title

A Graph Machine Learning Artifact for Money Laundering Network Detection in Fintech Transaction Graphs: Addressing Class Imbalance and Limited Labelled Data Under Financial Intelligence Unit Design Requirements.

## 02 Abstract

Money laundering detection in fintech ecosystems presents two compounding technical challenges: severe class imbalance (illicit transactions represent less than 1% of total volume) and scarcity of labelled data due to institutional confidentiality constraints. Existing rule-based and classical ML approaches fail to capture the relational structure of laundering networks, where the pattern of connections — not individual transactions — carries the signal. This study applies a Design Science Research framework to design, implement, and evaluate a Graph Machine Learning (GML) artifact that addresses these challenges. Design requirements are derived from the operational context of Financial Intelligence Units (FIUs). The artifact is implemented and evaluated on publicly available benchmark datasets (IBM AML Synthetic, Elliptic). Expected contributions include a reproducible GML architecture, a comparative evaluation protocol, and design principles transferable to FIU operational contexts.

## 03 Introduction & Problem Statement

Financial intelligence units face a structural detection problem: laundering networks operate through chains of apparently legitimate transactions whose illicit nature only becomes visible at the network level. Traditional detection systems — rule-based or transaction-level ML — miss this relational dimension entirely.

Graph Machine Learning offers a theoretically grounded solution: by modeling transactions as edges and accounts as nodes, GML methods can propagate suspicious signals across the network topology. However, two obstacles limit practical application: (1) class imbalance so extreme that standard models collapse to predicting the majority class, and (2) labeled data scarcity that makes supervised learning brittle.

No published work has systematically addressed both constraints simultaneously within a DSR framework that derives requirements from FIU operational practice. This gap — between the technical capability of GML and its validated application under real-world institutional constraints — is the problem this thesis addresses.

## 04 Literature Review

The review will cover GNN applications in fraud and AML detection (Elliptic, IBM AML dataset), relevant architectures, with focused in XAI methods applied to graph models in regulatory contexts. Key gaps to be addressed include: the scarcity of studies focused on Latin American VASPs, FIU institutional contexts, the absence of interpretability frameworks enforceable by financial supervisors, and the limitations of currently available public datasets.

## 05 Research Questions / Hypotheses

**Primary research question:**

How can a graph machine learning artifact be designed, implemented, and evaluated to improve the detection of money laundering networks in fintech transaction graphs, under conditions of class imbalance and limited labelled data — with design requirements derived from the operational context of financial intelligence units?

**Working hypothesis:**

H1: A GML architecture combining graph attention mechanisms with cost-sensitive training will achieve significantly higher F1-score on illicit class detection than baseline GCN under equivalent label availability (p < 0.05).

## 06 Methodology

The research will follow the Design Science Research framework (Hevner et al., 2004) across five phases: (1) systematic literature review, (2) dataset construction (Elliptic, synthetic data, and potentially real data), (3) GNN architecture design and implementation, (4) comparative evaluation against tabular ML baselines using AML-relevant metrics (F1, AUC-ROC, minority-class precision), and (5) extraction of generalizable design principles considering a FIU institutional context.


## 07 Ethical Considerations

Any use of real financial data will be subject to anonymization protocols, institutional confidentiality agreements, and compliance with Peru's legal framework. Synthetic datasets will be calibrated using publicly available typologies without exposing identifiable individuals or entities.

## 08 Expected Results

- A typology of FIU design requirements for GML-based AML detection — publishable as a standalone contribution.
- A comparative benchmark of GML architectures under class imbalance and label scarcity on synthetic dataset — with full reproducibility package.
- A best-performing artifact demonstrating statistically significant improvement over baselines.
- A set of transferable design principles connecting technical performance to FIU operational requirements.
- Open-source repository with documented code, experiment configurations, and results — registered on OSF.


## 09 Timeline & Budget

The schedule is organized across four phases spanning three years: (1) SLR and methodological design (months 1–6), (2) dataset construction and preprocessing (months 7–12), (3) model development and evaluation (months 13–24), and (4) institutional validation, writing, and defence (months 25–36). The budget covers cloud GPU infrastructure for model training, access to specialized databases, and, if possible, participation in international conferences (NeurIPS, ECML, ACFE).


## 10 Bibliography

- Bronstein, M. M., Bruna, J., Cohen, T., & Veličković, P. (2021). Geometric deep learning: Grids, groups, graphs, geodesics, and gauges. arXiv. https://arxiv.org/abs/2104.13478

- Hamilton, W. L., Ying, R., & Leskovec, J. (2017). Inductive representation learning on large graphs. arXiv. https://arxiv.org/abs/1706.02216

- Kipf, T. N., & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. arXiv. https://arxiv.org/abs/1609.02907

- Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., & Bengio, Y. (2018). Graph attention networks. arXiv. https://arxiv.org/abs/1710.10903

- Weber, M., Domeniconi, G., Chen, J., Weidele, D. K. I., Bellei, C., Robinson, T., & Leiserson, C. E. (2019). Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics. arXiv. https://arxiv.org/abs/1908.02591

- Bellei, C., Xu, M., Phillips, R., Robinson, T., Weber, M., Kaler, T., Leiserson, C. E., Arvind, & Chen, J. (2024). The shape of money laundering: Subgraph representation learning on the blockchain with the Elliptic2 dataset. arXiv. https://arxiv.org/abs/2404.19109
