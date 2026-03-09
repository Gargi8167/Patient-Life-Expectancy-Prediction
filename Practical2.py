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
