# Retracted Paper Analysis

## Section 1 — Paper metadata

| Field | Detail |
|---|---|
| **Title** | Using an Optimized Learning Vector Quantization-(LVQ-)Based Neural Network in Accounting Fraud Recognition |
| **Authors** | Yuan Zheng, Xiaolan Ye, Ting Wu |
| **Affiliations** | Anhui University of Finance and Economics; Southwestern University of Finance and Economics; ZhongYuan University of Technology |
| **Venue** | *Computational Intelligence and Neuroscience* (Hindawi/Wiley) |
| **Published** | June 29, 2021 |
| **Retracted** | June 28, 2023 |
| **DOI (original)** | 10.1155/2021/4113237 |
| **DOI (retraction notice)** | 10.1155/2023/9816186 |
| **Retraction notice** | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10322300/ |
| **Time between publication and retraction** | Approximately 2 years |

---

## Section 2 — The violation

**Classification:** Paper mill / peer-review manipulation + multiple publication-process integrity failures.

The retraction notice states that the investigation uncovered evidence of one or more of the following: discrepancies in scope, discrepancies in the description of the research reported, discrepancies between the availability of data and the research described, inappropriate citations, incoherent or meaningless content, and peer-review manipulation.

The notice reads: *"This investigation has uncovered evidence of one or more of the following indicators of systematic manipulation of the publication process [...] The presence of these indicators undermines our confidence in the integrity of the article's content and we cannot, therefore, vouch for its reliability."*

Using the session taxonomy, the primary classification is **peer-review manipulation**, with secondary indicators of **fabrication or falsification** (discrepancies between available data and described research) and potentially **incoherent/AI-generated content** (incoherent, meaningless, or irrelevant content). The notice explicitly states: *"We have not investigated whether authors were aware of or involved in the systematic manipulation of the publication process"* — meaning Hindawi cannot determine whether the authors themselves were culpable or whether they were victims of a compromised review pipeline.

This vagueness is itself a finding. A retraction notice that cannot name the specific violation or implicate the authors provides almost no information to the research community about what went wrong. It cannot be cited as evidence of a specific misconduct type — only as evidence that the publication process was compromised.

---

## Section 3 — Detection

The violation was detected by Hindawi's own Research Integrity and Research Publishing teams, with contributions from anonymous and named external researchers and research integrity experts. It was not caught by the original peer reviewers — detection came from a post-publication institutional sweep, not from content scrutiny.

This is characteristic of the broader Hindawi crisis: between 2022 and 2024, Wiley retracted more than 11,300 papers from the Hindawi portfolio and closed 19 journals after discovering systematic manipulation of special-issue peer-review pipelines. The signal that triggered investigation was volume and pattern, not the content of any individual paper. This particular article was one of thousands swept up in that process — it was not singled out because a reader found a specific error.

Detection came approximately 2 years after publication. During those 2 years, the paper was indexed, potentially cited, and available to researchers in the fraud detection field as a legitimate scientific contribution.

---

## Section 4 — Systemic analysis

Three structural factors made this possible:

**1. The APC-funded special issues model.** Hindawi journals operate on an article processing charge (APC) model: authors pay to publish. Special issues, guest-edited by external academics, created a pipeline where guest editors controlled reviewer assignment without robust editorial oversight. This is a documented vulnerability: when revenue depends on article volume and guest editors are not employees of the publisher, the incentive structure favors acceptance over rigor. The paper was published in a special issue of *Computational Intelligence and Neuroscience* — a journal that issued hundreds of retractions from the same pipeline.

**2. Reviewer workload and low friction for manipulation.** Peer review is unpaid, and reviewers frequently manage multiple simultaneous assignments. A fraudulent review — submitted by a fake reviewer identity or a colluding peer — is structurally indistinguishable from a legitimate one at the editorial level unless the publisher actively verifies reviewer identities and independence. Hindawi's investigation found that reviewer assignment itself had been manipulated, not merely reviewer conduct.

**3. The fraud detection field's incentive to publish.** Applied ML fields such as fraud detection, medical imaging, and financial risk modeling have seen disproportionate concentrations of retracted papers in the Hindawi portfolio. The domain is technically accessible, empirically checkable only with proprietary data, and produces results that are difficult to falsify externally. A paper claiming improved fraud recognition rates using a neural network variant is not easily challenged without access to the same dataset — and in this case, the retraction notice itself flags discrepancies between the data described and the data available.

This is the structure a doctoral researcher inherits: a publication ecosystem where volume is incentivized, review is underpaid and unverifiable, and applied results in closed-data domains are hard to scrutinize post-publication.

---

## Section 5 — Forensic check

A full forensic check (Benford's law, terminal-digit analysis, GRIM) would require access to the raw numerical data reported in the paper. The paper reports classification accuracy and fraud recognition rates for the LVQ model on a sample of 500 Chinese listed companies (2015–2019). However, the data source — the China Securities Regulatory Commission violation database — is not publicly available outside China, and the paper provides only aggregate performance metrics rather than case-level data.

The retraction notice itself flags "discrepancies between the availability of data and the research described," which is the most informative forensic signal available without the raw data: the numbers reported may not correspond to a dataset that existed or was accessible as described. Absence of verifiable data is not the same as fabricated data, but it prevents independent replication — which is, by the definition used in this course, a reproducibility failure regardless of the retraction status.

---

## Section 6 — Personal transfer

The single checkable practice I will adopt as a direct result of this analysis: before citing any paper from a Hindawi/Wiley journal published between 2019 and 2024, I will verify its current retraction status against the Retraction Watch database on the day I cite it, and record the verification date in my Zotero notes field. Retraction status changes — a paper that was valid when I added it to my reading list may have been retracted by the time I submit. This check is logged, not just intended.


