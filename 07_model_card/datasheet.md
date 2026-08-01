# Datasheet for the Elliptic Bitcoin Dataset (Classic Version)

## Motivation and composition

The Elliptic Bitcoin Dataset is a publicly available graph dataset of Bitcoin transactions
used as a benchmark for anti-money laundering (AML) research. It was released by Elliptic
and co-authored by Weber et al. (2019) to support financial forensics research using Graph
Neural Networks. In this project it is used as the primary dataset for reproducibility
practice and as the evaluation environment for the doctoral thesis GNN-AML artifact.

The dataset represents a transaction network: each node is a Bitcoin transaction, and each
directed edge represents a flow of Bitcoin between transactions. Node labels indicate
whether a transaction is illicit, licit, or unknown.

## Dataset composition

| Aspect | Record |
|---|---|
| Unit of analysis | One Bitcoin transaction node |
| Total nodes | 203,769 |
| Total edges | 234,355 |
| Node features | 166 anonymized features per node |
| Labeled nodes | ~46,564 (~23% of total) |
| Illicit nodes (labeled) | ~4,545 (~2% of labeled) |
| Licit nodes (labeled) | ~42,019 (~90% of labeled) |
| Unknown nodes | ~157,205 (~77% of total) |
| Temporal steps | 49 (each node belongs to one timestep) |
| Direct identifiers | None — all features are anonymized |
| Version used | Classic Elliptic (not Elliptic++) |

## Collection and processing

The original dataset was collected by Elliptic from the Bitcoin blockchain. Transaction
nodes were labeled as illicit if associated with known darknet markets, ransomware, or
other illicit services identified through external intelligence. Licit nodes were associated
with known exchanges, wallet providers, and mining pools. Unlabeled nodes could not be
confirmed as either category.

The 166 node features include local features (transaction-level statistics such as
transaction fees, input/output counts, and aggregated neighbor statistics) and a smaller
set of aggregated features derived from neighboring nodes. Feature names and exact
definitions are not disclosed by the dataset authors to protect proprietary information.

In this project, the dataset is accessed via Kaggle, tracked with DVC, and stored on
Google Drive as the DVC remote. The raw files are not committed to Git. The DVC pointer
and SHA-256 checksum logged in MLflow provide version traceability.

## Recommended use

Use this dataset for methodological research on graph-based fraud detection, reproducibility
demonstrations, and benchmark comparisons. It is appropriate for evaluating GNN
architectures on imbalanced node classification tasks in a financial network context.

Consult the original paper (Weber et al., 2019) and the dataset documentation before
analysis. Acknowledge the partial labeling and class imbalance as structural properties of
the data, not as errors.

## Prohibited or cautionary use

Do not use this dataset to make claims about current Bitcoin network behavior or
contemporary cryptocurrency fraud patterns. The dataset reflects a specific historical
window; the labeled transactions correspond to illicit activity identified at the time of
collection, and the threat landscape has evolved significantly since then.

Do not attempt to re-identify transaction originators or link this dataset to external
on-chain data to deanonymize individuals. Do not treat model performance on this benchmark
as evidence of operational AML capability in a live financial system.

Do not use unknown-labeled nodes as negative examples — their label is absent, not
confirmed licit.

## Variables and labels

**Primary label:** Binary node classification — illicit (1) vs. licit (0). Unknown nodes
are excluded from labeled experiments. The label reflects association with known illicit or
licit entities at the time of dataset construction, not a ground-truth legal determination.

**Features:** 166 anonymized continuous features. Feature 1 is the timestep index (1–49).
Features 2–94 are local transaction features. Features 95–166 are aggregated neighborhood
features. Exact feature definitions are not publicly available.

**Temporal structure:** Each node is assigned to one of 49 timesteps corresponding to
approximately two-week intervals. This structure enables temporally honest evaluation
(train on early timesteps, test on later ones).

## Known limitations and biases

**Class imbalance.** The labeled subset is severely imbalanced (~2% illicit). Classifiers
that optimize for accuracy can perform well while missing most illicit transactions.
Precision, recall, and F1 on the illicit class are the more informative metrics for
AML use cases.

**Partial labeling.** ~77% of nodes have no label. The labeled subset is not a random
sample of the full network. Models trained on labeled nodes may not generalize to the
unlabeled portion of the graph.

**Label construction.** Illicit labels are based on association with known entities, not
on direct observation of illegal activity. This introduces noise and potential false
negatives (illicit transactions not linked to known entities are labeled unknown, not
illicit).

**Feature opacity.** The anonymization of feature names prevents interpretability analysis
and limits the ability to diagnose model behavior in domain terms.

**Historical scope.** The dataset reflects Bitcoin network patterns from a specific
historical period. It should not be treated as representative of current cryptocurrency
fraud tactics, network topology, or regulatory context.

## Maintenance and distribution

The Elliptic Bitcoin Dataset is maintained by Elliptic and hosted on Kaggle. It is publicly
available at: https://www.kaggle.com/datasets/ellipticco/elliptic-data-set

In this project, the dataset is not committed to Git. It is represented by a DVC pointer
file and retrieved from the Google Drive DVC remote via `dvc pull`. The MLflow tracking
records store the dataset SHA-256 checksum alongside each experiment run to ensure version
traceability.

## Citation

Weber, M., Domeniconi, G., Chen, J., Weidele, D. K. I., Bellei, C., Robinson, T., &
Leiserson, C. E. (2019). Anti-money laundering in Bitcoin: Experimenting with graph
convolutional networks for financial forensics. *arXiv preprint arXiv:1908.02591.*
https://arxiv.org/abs/1908.02591
