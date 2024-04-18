# Using Predictive Analysis to Predict Diagnosis of a Breast Tumor

## Problem Statement
Breast cancer is the foremost malignancy affecting women, representing almost one-third of all cancers diagnosed in women in the United States. It stands as the second most frequent cause of cancer-related death among women. This type of cancer emerges from abnormal cell growth within breast tissue, typically forming a tumor. It's crucial to note that not all tumors are cancerous; they can be benign, pre-malignant, or malignant. Diagnosis often involves tests like MRI, mammogram, ultrasound, and biopsy.

## Expected Outcome
Given that breast cancer can be diagnosed through a breast fine-needle aspiration (FNA) test, which is a relatively quick and straightforward procedure involving the removal of fluid or cells from a breast lesion or cyst using a fine needle similar to one used for blood sampling. With this in mind, a model can be developed to classify breast cancer tumors using two training classifications:
- 1 = Malignant (Cancerous) - Present
- 0 = Benign (Not Cancerous) - Absent

## Objective
Since the labels in the data are discrete, the prediction falls into two categories, (i.e., Malignant or benign). In machine learning, this is a classification problem.

## Project Steps
1. Problem Definition (Breast Cancer data).
2. Loading the Dataset.
3. Analyze Data (same scale but different distributions of data).
4. Evaluate Algorithms (KNN looked good).
5. Evaluate Algorithms with Standardization (KNN and SVM looked good).
6. Algorithm Tuning (K=19 for KNN was good, SVM with an RBF kernel and C=100 was best).
7. Finalize Model (use all training data and confirm using validation dataset).

## Additional Information
- Used predictive modeling with Support Vector Machine (SVM).
- Utilized classification with cross-validation.
- Evaluated model accuracy using the Receiver Operating Characteristic (ROC) curve.
- Automated the machine learning process using pipelines.
