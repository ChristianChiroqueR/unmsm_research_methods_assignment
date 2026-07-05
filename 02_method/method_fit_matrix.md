# Assignment 2: Method Selection

**Student:** Christian Chiroque Ruiz  

**Instructor:** Dr. Loveleen Gaur  

**Date:** June 2026


## 1. Refined Research Question

How can a graph machine learning artifact be designed, implemented, and evaluated to improve the detection of money laundering networks in fintech transactions networks with class imbalance and limited labeled data?

## 2. Three Candidate Methods

| N° | Method | Description |
|---|---|---|
| 1 | **Design Science Research** | Construction and iterative evaluation of a graph machine learning artifact — a model or framework designed to detect money laundering networks in fintech transaction data. Following Hevner's seven guidelines, the artifact goes through build-evaluate-refine cycles, with evaluation conducted against real or synthetic representative data under conditions of class imbalance and limited labeled cases. The contribution is dual: the artifact itself and the design knowledge generated during its development. |
| 2 | Experimental (Quasi) | Systematic comparison of GNN architectures against traditional ML baselines (e.g., Random Forest, XGBoost, MLP) on benchmark datasets with class imbalance and limited labeled data. Without random assignment of subjects to conditions, this is a quasi-experiment — not a true experiment — where conditions are defined by model type and dataset configuration. |
| 3 | Case Study | A case study would investigate in depth how a FIU or fintech compliance team currently detects and analyzes money laundering networks — their processes, analytical tools, decision criteria, and limitations. Data sources would include interviews with analysts, observation of workflows, and internal documents. |

## 3. E.D.F.C.V. Scoring Matrix (1–5 per criterion)

| Criterion | What it asks | Method 1 | Method 2 | Method 3 |
|---|---|---|---|---|
| E - Epistemological fit | Does the method match the DS paradigm? | 5 | 2 | 1 |
| D - Data availability | Can the required data be accessed realistically? | 3 | 4 | 3 |
| F - Feasibility | Can it be done well within the present course stage? | 4 | 5 | 3 |
| C - Contribution type | Does it answer the actual question being asked? | 5 | 2 | 1 |
| V - Venue fit | Does it fit likely financial intelligence venues? | 4 | 3 | 2 |
| **Total** | | **21** | **16** | **10** |

## 4. Why Method 1 Wins

The research question was formulated with DSR logic, so the epistemological alignment is near-perfect. The artifact (a GML model/framework) addresses a real, important problem (Hevner Guideline 2), and the evaluation strategy — comparing against baselines under class imbalance conditions — satisfies Guideline 3. The main viability risk is data access: if real fintech data cannot be obtained, the external validity of the artifact's evaluation weakens. This is manageable by using established synthetic benchmarks combined with a clearly argued limitation section. Viable, contingent on resolving data access before committing.

## 5. Why Method 2 Does Not Win

Partial fit. This method answers a narrower question than the one posed — it tells you which model performs better, not how to design an artifact that solves the problem. Its real value in your thesis is as the evaluation strategy embedded within DSR, not as a standalone method.


## 6. Why Method 3 Does Not Win

Low fit. Case study would answer the wrong question for your thesis. Its contribution — contextual understanding of current AML practices — has value as a motivating section or as requirements elicitation for the artifact design phase within DSR, but cannot stand alone as the primary method.
