# Credit Score Classification using Random Forest Tree

This Python script demonstrates how to use the Random Forest algorithm for credit score classification. Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees during training and outputting the mode of the classes for classification tasks.

## Prerequisites

- Python 3.x
- `numpy` library
- `pandas` library
- `scikit-learn` library (which includes the `RandomForestClassifier`)

## Installation

You can install the required libraries via pip:

```
pip install numpy pandas scikit-learn
```

## Usage

1. Clone this repository or download the `credit_score_classification_random_forest.ipynb` file.
2. Ensure that you have the required libraries installed.


## Dataset

This script uses a sample dataset containing information about individuals and their credit scores. The dataset is stored in a CSV file named `data.csv` from https://statso.io/credit-score-classification-case-study/. You can replace this file with your own dataset following the same structure if desired.

## Random Forest Classification

The script reads the dataset, preprocesses it, splits it into training and testing sets, and then fits a Random Forest Classifier to the training data. It evaluates the classifier's performance on the test set and displays the classification report, including precision, recall, F1-score, and support.

## Contact

For any issues or suggestions regarding this script, feel free to contact Alexander at b_alx_arboleda@outlook.com.

