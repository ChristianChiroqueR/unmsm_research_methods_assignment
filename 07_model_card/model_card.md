# Model Card: Exploratory Elliptic Bitcoin AML Classifier

## Model details

One model is trained in `05_pipeline/src/train.py`: logistic regression applied to the
node-level feature matrix of the Elliptic Bitcoin Dataset. It predicts whether a Bitcoin
transaction node is illicit, licit, or unknown (unknown-class nodes are excluded from
training and evaluation). Logistic regression serves as the reproducible baseline for this
course artifact; a Graph Neural Network (GNN) implementation is the target architecture for
the doctoral thesis and is documented separately in the thesis protocol.

Fixed seeds are 13, 21, 42, 87, and 100. Experiments are tracked in MLflow under the
experiment name `elliptic-aml-pipeline`.

## Intended use

The intended use is a course demonstration of reproducible preprocessing, experiment
tracking, and versioned data management applied to a financial forensics benchmark. The
pipeline may support exploratory discussion of which aggregated transaction features carry
signal for illicit-activity classification in the Elliptic graph.

This artifact also serves as the reproducibility baseline against which the GNN
implementation in the doctoral thesis will be compared.

## Out-of-scope use

Do not use this model for real-time transaction screening, individual account risk scoring,
regulatory action, law enforcement reporting, or any operational anti-money laundering
decision. It is not validated for deployment in a financial intelligence unit or any
production environment. The Elliptic dataset reflects Bitcoin network activity from a
specific historical window and does not represent current cryptocurrency fraud patterns.

## Inputs and output

**Inputs:** 166 anonymized node-level features per transaction node. The original feature
meanings are not disclosed by the dataset authors; features include local and aggregated
transaction statistics. The temporal step index (1–49) is available but not used as a
training feature in the baseline pipeline.

**Output:** A probability score and a thresholded binary label: illicit (1) or licit (0).
Unknown-class nodes (approximately 77% of the dataset) are excluded from both training
and evaluation.

## Evaluation design

Each experiment uses a stratified 75/25 train-test split on the labeled subset. Imputation
and scaling are fitted inside the pipeline on training data only; no transformation is
fitted on test data. MLflow stores seed, model type, dataset identity, Git commit hash,
and all metrics for every run.

Across the five fixed seeds, the logistic regression baseline achieved:

| Metric | Mean across 5 seeds |
|---|---|
| Accuracy | ~0.96 |
| Seeds used | 13, 21, 42, 87, 100 |

These values describe one internal exploratory task only on a public benchmark. They are
not a measure of operational effectiveness, calibration across transaction types, or
generalizability to live financial networks.

## Known limitations and risks

**Class imbalance.** The labeled subset of Elliptic is severely imbalanced (~2% illicit
nodes). High accuracy can be achieved by a classifier that rarely predicts illicit — the
relevant metrics for AML tasks are precision, recall, and F1 on the illicit class, which
are lower than overall accuracy.

**Partial labeling.** Approximately 77% of nodes have no label. The labeled subset is
not a random sample of all transactions; this limits generalizability claims.

**Feature opacity.** The 166 features are anonymized. Interpretability analysis is not
possible without knowledge of the underlying feature definitions.

**Temporal structure ignored in baseline.** The 49 timesteps encode a natural temporal
ordering. The logistic regression baseline does not exploit this structure; the GNN
implementation in the thesis addresses it explicitly.

**Dataset age.** The Elliptic dataset captures Bitcoin network activity from a specific
historical period. Money laundering tactics and network topology evolve over time; this
artifact is a methodological demonstration, not a current operational tool.

## Version, ownership, and training record

| Item | Recorded value |
|---|---|
| Version | Course artifact, Elliptic classic build — 2026 |
| Owner | Christian Chiroquer (ChristianChiroqueR) |
| Framework | scikit-learn 1.5.2 / PyTorch (GNN phase) |
| Training population | Labeled nodes only (~46,564 of 203,769 total) |
| Outcome | Binary: illicit (1) vs. licit (0) |
| Data version evidence | DVC pointer, dataset SHA-256 logged in MLflow |
| Reproducibility evidence | Five fixed seeds, pinned dependencies, Git commit, MLflow records |

## Reported internal performance

| Model | Mean accuracy | Seeds |
|---|---|---|
| Logistic regression (baseline) | ~0.96 | 13, 21, 42, 87, 100 |

These are mean values across five fixed internal splits. They should not be interpreted
as evidence of operational AML detection capability or compared with clinical/regulatory
benchmarks without appropriate context.

## Evaluation factors

The labeled subset contains two classes: illicit and licit. Given the severe class
imbalance, accuracy alone is a misleading summary statistic. Future versions of this
pipeline will report F1, precision, recall, and AUC-ROC on the illicit class as primary
metrics, consistent with the evaluation design of the GNN thesis artifact.

Temporal generalization (training on early timesteps, evaluating on later ones) is an
important evaluation factor for this dataset and will be addressed in the GNN
implementation.

## Deployment and monitoring decision

This artifact is not approved for deployment. No API, score report, or automated
decision should be built from it. A production AML system would require independent
validation on held-out financial networks, regulatory review, calibration assessment,
stakeholder consultation, and an explicit monitoring and drift-detection plan. Any
future model update must create a new versioned data and model record rather than
overwriting these results.
