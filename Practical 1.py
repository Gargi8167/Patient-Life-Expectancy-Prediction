PROBLEM STATEMENT:

Predict whether a patient is at high risk of early death based on their current health condition.
# ===================================================================================================================

1) Business Problem Statement

Hospitals need to identify patients who are at high risk of early death (within the next 12 months) based on their current health condition, medical history, and clinical indicators.
This helps doctors take early preventive action, plan treatments, monitor critical patients closely, and improve overall survival outcomes.

2) Simplified Context of the Problem

Patients with similar diseases often have very different survival outcomes depending on:
- Age
- BMI
- Comorbidities
- Lifestyle
- Clinical parameters
- Lab test values

Manually identifying which patient is at high death risk is difficult and often inaccurate.
A machine learning model can analyze complex health patterns and provide early warnings.

3) Problem Identification
Currently, early death risk assessment is:
- Based on doctor’s experience
- Time-consuming and subjective
- Not always accurate
- May fail to identify “silent high-risk” cases
Without an AI system, hospitals may miss critical patients who need immediate monitoring and emergency care.

4) Business Objective
Main Goal:
Predict whether a patient belongs to the High-Risk Early Death category or Low-Risk category.

Maximize:
- Correct identification of high-risk patients
- Prediction reliability and medical usefulness

Minimize:
- False negatives (missing high-risk patients)
- Incorrect predictions that lead to poor medical decisions

5) Stakeholder Expectations
Doctors:
- Need an accurate decision-support system
- Want to identify high-risk patients early
- Expect interpretable results

Hospitals:
- Want reduced mortality rates
- Desire better resource allocation
- Need a reliable AI tool for triage

Patients & Families:
- Expect timely treatment and risk awareness
- Want clarity and early warning for better preparation

6) Constraints & Limitations
- Patient data privacy must be strictly maintained (HIPAA, GDPR)
- Missing or incomplete medical information may affect accuracy
- Ethical concerns about predicting death risk
- Imbalanced data (fewer high-risk patients)
- High cost and technical expertise required for deployment

7) Feasibility Check
Yes, the problem is feasible using supervised classification models, such as:
- Logistic Regression
- KNN
- Naive Bayes
- Decision Tree
- Random Forest
- Bagging / Boosting (AdaBoost, Gradient Boosting, XGBoost)
- Stacking Classifiers
Model can be trained using features such as age, BMI, comorbidities, lifestyle factors, symptoms, and lab results.

8) Success Criteria
Business Success:
- Early identification of high-risk patients
- Improved patient survival
- Better treatment planning and monitoring

ML Success:
- High Recall for high-risk class
- High F1-score & ROC-AUC
- Low false-negative rate
- Good generalization on new hospital data

9) Business Impact
By accurately predicting high-risk patients:
- Doctors can start early intervention
- Hospitals can prioritize critical cases
- Patients receive timely treatment
- Families can plan and prepare
- Overall mortality rates decrease
- Healthcare quality improves
This creates a life-saving, decision-support system for medical professionals.


# =============================================================================
  PRACTICAL - 02 (DATA DICTIONARY)
# 2. Explore the dataset to gain insights into its structure, features, and quality.
# =============================================================================

--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
Feature Name              |          Description                          |      Type                  |            Relevance                        |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
patient_id                | Unique identifier for each patient            | Numerical, Discrete        | Irrelevant, Indexing only                   |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
age                       | Age of patient in years                       | Numerical, Continuous      | Relevant – higher age → lower survival      |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
sex                       | Biological sex of patient                     | Categorical, Nominal       | Relevant demographic factor                 |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
weight_kg                 | Weight of patient (kg)                        | Numerical, Continuous      | Relevant – health indicator, used in BMI    |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
height_cm                 | Height of patient (cm)                        | Numerical, Continuous      | Relevant indirectly, used for BMI           |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
bmi                       | Body Mass Index                               | Numerical, Continuous      | Important – obesity/underweight impact      |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
smoking_status            | Smoking habit (Never/Former/Current)          | Categorical, Nominal       | Very Relevant lifestyle risk factor         |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
alcohol_use               | Alcohol consumption pattern                   | Categorical, Nominal       | Relevant lifestyle factor                   |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
bp_systolic               | Systolic blood pressure                       | Numerical, Continuous      | Relevant – cardiovascular health            |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
bp_diastolic              | Diastolic blood pressure                      | Numerical, Continuous      | Relevant – cardiovascular health            |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
heart_rate                | Resting heart rate                            | Numerical, Discrete        | Relevant – indicates heart stress           |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
cholesterol_total         | Total cholesterol level                       | Numerical, Continuous      | Relevant – predictor of heart disease       |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
hba1c                     | HbA1c (blood sugar control)                   | Numerical, Continuous      | Important – diabetes risk                   |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
creatinine                | Serum creatinine (kidney function)            | Numerical, Continuous      | Important – kidney health                   |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
hemoglobin                | Hemoglobin level                              | Numerical, Continuous      | Relevant – blood oxygen capacity            |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
platelets                 | Platelet count                                | Numerical, Discrete        | Relevant – clotting/cancer risk             |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
diagnosis                 | Primary disease (Cancer, COPD, CKD, etc.)     | Categorical, Nominal       | Crucial – defines survival condition        |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
disease_stage             | Stage/Severity of disease                     | Categorical, Ordinal       | Highly Relevant – direct survival factor    |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
treatment_type            | Treatment given (Surgery, Medication, etc.)   | Categorical, Nominal       | Relevant – impacts survival duration        |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
comorbidities_count       | Number of coexisting diseases                 | Numerical, Discrete        | Relevant – more comorbidities = higher risk |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
recent_hospitalizations   | Number of recent hospitalizations             | Numerical, Discrete        | Relevant – reflects instability             |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
last_followup_days        | Days since last follow-up                     | Numerical, Discrete        | Less Relevant – used for censoring only     |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
survival_months           | Time survived after diagnosis/treatment       | Numerical, Continuous      | Target Variable – remaining life measure    |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
event                     | Patient died (1) or censored (0)              | Binary                     | Target Variable – survival outcome          |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
risk_category             | Risk level assigned (Low/Moderate/High/etc.)  | Categorical, Ordinal       | Derived feature – useful for classification |
--------------------------|-----------------------------------------------|----------------------------|---------------------------------------------|
