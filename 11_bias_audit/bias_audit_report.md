# Bias Audit Report — COMPAS Recidivism Dataset

## 1. Setup

| Field | Value |
|---|---|
| **Dataset** | COMPAS Two-Year Recidivism (ProPublica, 2016) |
| **Protected attribute** | Race |
| **Privileged group** | Caucasian (race = 1) |
| **Unprivileged group** | African-American (race = 0) |
| **Favorable outcome** | Did not re-offend within two years (label = 0.0) |
| **Train / test split** | 70 / 30, shuffle=True, seed=42 |
| **Train rows** | 4,316 |
| **Test rows** | 1,851 |
| **Toolkit** | IBM AI Fairness 360 (aif360==0.6.1) |
| **Baseline model** | Logistic Regression (scikit-learn, max_iter=1000) |

**Context.** COMPAS is a commercial risk-scoring tool used by US judges to predict
recidivism. ProPublica (2016) documented that African-American defendants were flagged
as high-risk at roughly twice the rate of white defendants who did not re-offend. This
audit replicates that finding on the public two-year dataset and applies a pre-processing
mitigation to reduce the disparity.

---

## 2. Bias in the raw data (before any model)

Before training any classifier, the training set itself already encodes a disparity:

| Metric | Value |
|---|---|
| Disparate impact (data) | 0.850 |
| Statistical parity diff (data) | -0.090 |

The favorable outcome (not re-offending) is distributed unequally across racial groups
in the raw data. African-American defendants receive the favorable label at a rate 9
percentage points lower than Caucasian defendants. A classifier trained on these data
will inherit this disparity.

---

## 3. Before metrics (baseline model, no mitigation)

| Metric | Value | Reading |
|---|---|---|
| **Accuracy** | 0.664 | |
| **Disparate impact** | 0.773 | **FAIL (< 0.8): potential disparate impact** |
| **Statistical parity difference** | -0.165 | African-American defendants predicted favorable 16.5pp less often |
| **Equal opportunity difference** | -0.095 | True positive rate 9.5pp lower for African-Americans |
| **Average odds difference** | -0.139 | Average error gap across both error types |

**Four-fifths rule: FAIL.** A Disparate Impact below 0.8 is the regulatory threshold for
potential discriminatory selection rates (e.g. NYC Local Law 144). The baseline model
at 0.773 falls below this threshold, confirming the disparity documented by ProPublica.

The model amplifies the bias already present in the data: the raw data showed a
Disparate Impact of 0.850 (marginal pass), but the trained classifier drops it further
to 0.773 (clear fail).

---

## 4. Mitigation applied

| Field | Value |
|---|---|
| **Method** | Reweighing (pre-processing) |
| **Library** | `aif360.algorithms.preprocessing.Reweighing` |
| **Fairness metric targeted** | Disparate Impact / Statistical Parity Difference |
| **How it works** | Computes per-instance weights so that each group × label combination contributes equally to training. Does not alter features or labels — only the sample weights passed to the classifier. |

**Why Reweighing for this context.** In a recidivism-prediction setting, the most
direct harm is a false positive for the unprivileged group: flagging an
African-American defendant as high-risk when they would not re-offend. Reweighing
targets Statistical Parity — equalizing the rate of favorable predictions across groups
— which directly addresses this asymmetric false-positive burden. It is also a
transparent, interpretable intervention: the adjustment is a weight table, not a
black-box transformation of the data.

---

## 5. After metrics and trade-off

| Metric | Before | After (Reweighing) | Change |
|---|---|---|---|
| **Accuracy** | 0.664 | 0.653 | -0.011 |
| **Disparate impact** | 0.773 | 0.975 | **+0.202** |
| **Statistical parity difference** | -0.165 | -0.016 | +0.149 |
| **Equal opportunity difference** | -0.095 | +0.031 | +0.126 |
| **Average odds difference** | -0.139 | +0.015 | +0.154 |

**Four-fifths rule: PASS (≥ 0.8).** Disparate Impact moved from 0.773 to 0.975 —
well above the regulatory threshold.

**The trade-off.** Accuracy fell by 1.1 percentage points (0.664 → 0.653). This is
the cost of the fairness gain: the reweighted model makes slightly more errors in
aggregate in order to distribute those errors more equally across racial groups.
There is no free lunch — stating this cost explicitly is part of an honest audit.

**The impossibility theorem in this result.** Chouldechova (2017) proved that when
base rates differ across groups — as they do in COMPAS — no classifier can
simultaneously achieve equal predictive value, equal false-positive rates, and equal
false-negative rates. This audit optimized for Statistical Parity (equal selection
rates). Northpointe's original defense of COMPAS optimized for Predictive Parity
(equal precision). Both readings are mathematically valid; the choice between them
is a moral and policy decision, not a technical one.

---

## 6. Recommendation

Before any recidivism-prediction model is deployed in a judicial context, the deploying
institution should specify which fairness metric it is optimizing — Statistical Parity,
Equal Opportunity, or Predictive Parity — and document the ethical justification for
that choice, because the impossibility theorem guarantees that satisfying one metric
will worsen another. The 1.1-point accuracy cost observed here is operationally
acceptable in a domain where a false positive (wrongly flagging a defendant as
high-risk) carries significant liberty consequences for the individual.

---

## 7. One honest limitation

This audit measures fairness along a single protected attribute (race) and a single
mitigation method (Reweighing). It does not examine intersectional subgroups
(e.g. young African-American women vs. older Caucasian men), a second protected
attribute (sex is also present in COMPAS), calibration across decile risk scores,
or the temporal stability of the fairness gains across different data splits. A
production audit would require all of these before a deployment recommendation
could be made.
