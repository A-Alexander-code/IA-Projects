# Online Payment Fraud Detection using Decision Tree Classifier

[Decision Tree](decision_tree.png)

## Overview

This repository contains a Python script implementing a Decision Tree Classifier model for detecting online payment fraud. The model is trained on a dataset containing various features related to online credit card transactions, such as transaction type, transaction amount, old balance of the sender's account, new balance of the sender's account, and a binary label indicating whether the transaction is fraudulent.

## Dataset

The dataset used for training the model is provided in `credit_card.csv`. It contains the following columns:

- `type`: Type of transaction (e.g., payment, transfer, etc.).
- `amount`: Amount of the transaction.
- `oldbalanceOrg`: Old balance of the sender's account before the transaction.
- `newbalanceOrig`: New balance of the sender's account after the transaction.
- `isFraud`: Binary label indicating whether the transaction is fraudulent (1 for fraud, 0 for legitimate).

## Contributions

Contributions to this project are welcome. If you find any errors or have suggestions for improvement, feel free to open an issue or submit a pull request.