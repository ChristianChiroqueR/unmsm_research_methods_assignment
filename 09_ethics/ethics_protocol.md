# Ethics Protocol — GML-Based AML Detection in Fintech Transaction Networks

## Ethical frame

This project follows the Belmont principles of respect for persons, beneficence, and
justice, as well as the Menlo Report extension of those principles to information and
communications technology research. It additionally aligns with CONCYTEC's Código de
Integridad Científica (2021) and the principles established in Peru's Ley N° 31814 (2023)
on artificial intelligence ethics.

The project uses the Elliptic Bitcoin Dataset, an anonymized public dataset of Bitcoin
transaction nodes with no personally identifiable information. It does not recruit, contact,
or intervene with any human participant. Low direct-contact risk does not remove ethical
responsibility: an AML detection system, even one trained on public benchmark data, produces
design decisions that could cause harm if misapplied — through false accusations, financial
exclusion, or surveillance overreach. This protocol documents those risks and the safeguards
that govern this research.

---

## Respect for persons and privacy

The pipeline uses only the Elliptic Bitcoin Dataset, which contains no personal data of
identifiable natural persons. Node features are fully anonymized (166 engineered features
with no disclosed meanings), and no linkage to external identity records is possible or
attempted. Ley N° 29733 (Peru, DS 016-2024-JUS) and GDPR both fall outside the scope of
this project because no personal data of natural persons is processed — this determination
is documented in the project's Data Management Plan.

The research involves no deception, no covert data collection, and no contact with
individuals. The dataset was collected and released by Elliptic with explicit permission for
academic use. The project will not attempt to deanonymize transaction originators, link
the Elliptic graph to external on-chain data to identify individuals, or share credentials
or access tokens.

All code, model weights, and experiment records will be published under CC-BY-4.0 upon
thesis defense, enabling independent scrutiny of every design decision documented here.

---

## Beneficence and non-maleficence

The expected benefit of this research is a documented, reproducible framework for
Graph Machine Learning applied to AML detection in financial transaction networks. The
framework is designed to support — not replace — human analysts in financial intelligence
units, and to make design decisions in GML-AML systems more transparent and auditable.

Key foreseeable risks are:

**False positives.** A model that incorrectly flags a licit transaction as illicit can
contribute to account freezes, regulatory investigations, or reputational damage for
legitimate businesses or individuals. This risk is heightened in deployment contexts even
when the model itself is trained on a research benchmark.

**False negatives.** A model that misses illicit transactions provides false assurance and
may reduce analyst vigilance. In AML contexts, false negatives can have regulatory and
societal consequences.

**Overconfidence in benchmark performance.** The Elliptic dataset reflects a specific
historical window of Bitcoin activity. Reporting high accuracy on this benchmark without
noting its limitations could mislead practitioners about operational readiness.

**Misuse of the framework.** A GML-AML framework designed for financial crime detection
could be repurposed for broader financial surveillance, profiling of lawful political
activity, or targeting of specific communities. This dual-use risk is documented explicitly
in the risk matrix below.

All outputs from this research — the model card, the thesis, and published artifacts — will
explicitly prohibit deployment in operational AML decisions without independent validation,
regulatory review, and institutional ethics approval.

---

## Justice

Bitcoin transaction networks are not demographically neutral. Illicit labels in the Elliptic
dataset reflect association with entities identified as darknet markets, ransomware operators,
or other services known at the time of collection. Labels are not a ground-truth legal
determination. A model trained on these labels encodes the detection priorities and
identification capacity of the labeling process — not an objective ground truth about
financial crime.

In deployment contexts (beyond this research), AML systems can impose disproportionate
burdens on specific transaction profiles, economic sectors, or geographic regions if base
rates of flagging differ across groups. The fairness impossibility theorem (Chouldechova,
2017) is directly relevant: when base rates differ across transaction segments, it is
mathematically impossible to simultaneously achieve equal false positive rates and equal
positive predictive values across groups. Choosing a fairness metric in an AML context is
therefore a moral and policy decision, not a purely technical one. This protocol documents
that choice as belonging to the institutional context of deployment — not to the research
benchmark — and explicitly warns against applying the framework to groups without
a subgroup-level fairness audit.

Observed differences in detection rates across transaction types, volume segments, or
network positions should be described as properties of the data and model design, not as
evidence that certain transaction profiles are inherently suspicious.

---

## Risk and safeguard matrix

| Risk | Why it matters | Safeguard | Escalation trigger |
|---|---|---|---|
| **Dual-use of the AML framework** | A GML system designed for money laundering detection could be repurposed for mass financial surveillance or targeting of lawful activity. | The thesis and model card explicitly restrict use to research and decision-support roles. Any deployment proposal requires independent ethics review. | Any proposal to deploy the model in an operational system outside the documented research scope. |
| **False positive harm** | Incorrectly flagging a licit transaction as illicit can cause account freezes, reputational damage, or regulatory action against legitimate entities. | The model card prohibits operational use. Results are reported with precision and recall on the illicit class, not accuracy alone. | Any request to use model output as direct evidence in a regulatory or legal proceeding. |
| **Benchmark overconfidence** | High accuracy on Elliptic (historical, anonymized, partial labels) does not imply operational readiness for live financial networks. | All communications about performance explicitly state dataset limitations, historical scope, and partial-label structure. | A result is presented without its stated limitations in a public or policy forum. |
| **Credential and data exposure** | Kaggle API tokens and GitHub tokens, if exposed, could grant unintended access to data pipelines or private repositories. | Credentials stored exclusively in Colab Secrets; never hardcoded in notebooks or committed to Git. | A credential appears in a Git commit, notebook output, or shared document. |
| **UIF conflict of interest** | The researcher works at a financial intelligence unit. Professional context informs design requirements but must not introduce non-public operational data. | All implementation uses public datasets only. UIF context is documented as a source of design requirements, not data. | Any proposal to incorporate non-public UIF data into the pipeline without institutional approval and ethics review. |
| **Temporal and domain mismatch** | Elliptic reflects historical Bitcoin activity. Generalizing conclusions to current fintech or traditional banking networks without validation is misleading. | The thesis frames Elliptic results as benchmark evidence, not operational claims. Domain transfer requires separate validation. | A result from the Elliptic pipeline is cited as evidence for a policy or operational decision in a different financial domain. |

---

## Belmont principles in practice

**Respect for persons** means using only data collected for public research use, not
attempting to reverse anonymization, and not making claims about individuals from
aggregate transaction patterns. In this project it also means acknowledging that the
entities represented in the Elliptic graph — however anonymized — include real economic
actors whose livelihoods could be affected by systems trained on this data.

**Beneficence** means that the goal of this research is to make AML detection more
transparent, reproducible, and auditable — not to maximize detection rates at any cost.
A framework that improves analyst oversight and reduces both false positives and false
negatives serves beneficence. A framework optimized for raw accuracy on an imbalanced
benchmark at the expense of interpretability does not.

**Justice** means that the costs and benefits of AML detection systems should not fall
disproportionately on any transaction segment, economic sector, or community. Designing
for justice requires choosing fairness metrics deliberately, documenting who bears the
error, and building redress mechanisms into any deployment design — even when the
research itself operates on a public benchmark.

---

## Accountability and review points

The repository owner (Christian Chiroquer) is responsible for checking dataset access
conditions, managing collaborator permissions, and documenting any material change to the
research scope in Git. Any collaborator who identifies a data-quality, privacy, or
interpretive concern should record it as a GitHub issue before results are shared beyond
the course.

Before thesis submission, public repository release, or journal submission, the author
will verify applicable UNMSM, CONCYTEC, and Ley N° 31814 requirements with the
appropriate institutional office. This course protocol does not constitute institutional
ethics approval and does not substitute for the review requirements that apply to
publication or deployment.

If the research scope expands to include: (a) non-public UIF data, (b) real-time
transaction data, (c) personally identifiable financial records, or (d) a deployment
proposal in an operational AML system — work stops until a new ethics and data governance
assessment is completed and documented.

---

## Data and participant boundary

This research begins after data collection. It does not alter the Elliptic dataset, seek
new consent, make contact with any individual, or return predictions to any entity. The
project will not claim to speak for the individuals or organizations whose transactions
are represented in the graph, infer the identity of a node from its features, or contact
any party because of a model prediction.

The Elliptic dataset is used solely within the documented research scope: reproducibility
practice, GNN architecture evaluation, and doctoral thesis development. Any extension
beyond this scope — including use of derivative models in a financial institution —
requires a separate governance process.

---

## Ethical analysis checkpoints

| Question before an action | Required response |
|---|---|
| Does the action involve linking the Elliptic graph to external data that could identify a transaction originator? | Stop. This is outside scope. A new ethics and data governance assessment is required. |
| Does a planned result report model performance without stating dataset limitations, partial labels, or historical scope? | Revise the result to include explicit scope statements before sharing. |
| Does a result describe a transaction type or network segment as inherently suspicious based on model output alone? | Rewrite the claim. State that model output reflects training data patterns, not ground truth. |
| Does a proposed use involve operational screening, automated account action, or regulatory reporting? | Do not use this research model. A separate clinical, legal, and institutional ethics process is required. |
| Does a collaborator need access to raw data, credentials, or the DVC remote? | Grant minimum necessary access, document the reason and duration, and revoke when no longer needed. |
| Does the research scope expand to include non-public UIF data or personally identifiable financial records? | Stop. A new institutional ethics review and data governance agreement are required before proceeding. |

---

## Justice in communication

Justice applies to language as well as to model design. Higher detection rates for a
particular transaction type, volume segment, or network position should be described as
properties of the training data and model architecture — not as evidence that those
segments are inherently associated with financial crime.

The framework developed in this thesis is designed for use by trained financial analysts
with domain knowledge, legal authority, and accountability structures. It is not designed
to automate enforcement decisions or to replace human judgment in AML investigations.

This protocol recognizes an evidence gap that persists beyond the benchmark: the Elliptic
dataset cannot capture the full social, economic, and regulatory context of money
laundering. If this research later informs a system proposed for deployment in a specific
financial context or jurisdiction, the stakeholders affected by that system — analysts,
regulated entities, and oversight bodies — must participate in the design and governance
of that next stage, rather than being represented only as nodes in a graph.
