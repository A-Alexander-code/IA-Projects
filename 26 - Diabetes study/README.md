<p align="center"> 
<a href="https://github.com/A-Alexander-code"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=A-Alexander-code&color=ff3300" alt="Last Commit"/></a> 
</p> 
<!--<img src="https://badges.pufler.dev/contributors/milaan9/01_Python_Introduction?size=50&padding=5&bots=true" alt="milaan9"/>-->

# Predictive Modeling for Binary Diabetes Classification: A Comparative Analysis of K-Nearest Neighbors, Neural Networks, and Logistic Regression



![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/medical-diagnosis-diabetes.jpg)<br>


## Overview

This project focuses on developing and comparing machine learning models for binary classification, specifically to predict a health outcome based on various diagnostic measurements. Using a dataset containing health-related features, such as blood glucose levels, BMI, and age, we aim to distinguish between positive and negative cases with accuracy and reliability. The project explores three different models—K-Nearest Neighbors (KNN), Binary Neural Network Classifier, and Logistic Regression—each offering unique strengths in terms of predictive power and interpretability.

## Libraries

The project leverages the following libraries:
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical operations.
- **Matplotlib** and **Seaborn**: For data visualization.
- **Scikit-Learn**: For implementing machine learning models (K-Nearest Neighbors, Logistic Regression) and calculating evaluation metrics.
- **TensorFlow/Keras**: For building and training the Binary Neural Network Classifier.

## Project Components

The project is divided into several components:

1. **Data Preprocessing**:
   - Handling missing values, normalizing and scaling features, and generating dummy variables to prepare the data for modeling.
   - Splitting the dataset into training and testing subsets to assess model performance.

2. **Modeling**:
   - **K-Nearest Neighbors (KNN)**: A distance-based classifier trained to capture local patterns in the data.
   - **Binary Neural Network Classifier**: A deep learning model designed to learn complex patterns and improve predictive accuracy.
   - **Logistic Regression**: A linear, interpretable model used as a baseline for comparison.

3. **Evaluation**:
   - Confusion matrices, accuracy scores, precision, recall, F1-scores, and AUC scores were calculated for each model to assess their performance.
   - Comparison of model results to highlight the strengths and limitations of each approach.


## Results

- **K-Nearest Neighbors**:
  - **Overall Accuracy**: 85%
  - **AUC Score**: 0.82626
  - **Precision (Class 0)**: 0.87, **Recall (Class 0)**: 0.89, **F1-Score (Class 0)**: 0.88
  - **Precision (Class 1)**: 0.79, **Recall (Class 1)**: 0.76, **F1-Score (Class 1)**: 0.78
  - Strong balance between sensitivity and specificity, with robust generalization for non-diabetic cases.

- **Binary Neural Network Classifier**:
  - **Test Accuracy**: 81.82%
  - **Test Loss**: 0.4483
  - **AUC Score**: 0.82626
  - **Maximum Training Accuracy**: 0.93279
  - **Maximum Validation Accuracy**: 0.9187
  - High training and validation accuracy indicate effective learning, though there is some evidence of overfitting.

- **Logistic Regression**:
  - Balanced performance with consistent classification for both diabetic and non-diabetic cases.
  - Provides strong interpretability, though with some limitations in capturing non-linear relationships in the data.


## Future Work

To enhance the effectiveness of these models, several future steps are recommended:

1. **Advanced Feature Engineering**: Additional derived features could reveal more intricate relationships and improve model performance.

2. **Model Optimization**:
   - Hyperparameter tuning, particularly for the neural network and KNN, could lead to more refined predictions and better generalization.
   - Experimenting with ensemble methods, combining strengths of different models, may yield higher accuracy and stability.

3. **Cross-Validation**: Implementing k-fold cross-validation to better assess generalization performance across different data subsets.

4. **Exploring Alternative Models**: Trying more complex models like Support Vector Machines (SVM) or Gradient Boosting to capture potentially non-linear patterns within the data.

5. **Addressing Imbalanced Data**: Techniques like SMOTE (Synthetic Minority Over-sampling Technique) could be applied to balance the classes, especially if there is a need to increase sensitivity for the positive class.

This project provides a solid foundation for health-related binary classification tasks, with insights that can contribute to real-world diagnostic applications.

## Frequently asked questions ❔

### How can I thank you for writing and sharing this tutorial? 🌷

You can <img src="https://img.shields.io/static/v1?label=%E2%AD%90 Star &message=if%20useful&style=style=flat&color=blue" alt="Star Badge"/> and <img src="https://img.shields.io/static/v1?label=%E2%B5%96 Fork &message=if%20useful&style=style=flat&color=blue" alt="Fork Badge"/> Starring and Forking is free for you, but it tells me and other people that it was helpful and you like this tutorial.

Go [**`here`**](https://github.com/A-Alexander-code/IA-Projects) if you aren't here already and click ➞ **`✰ Star`** and **`ⵖ Fork`** button in the top right corner. You'll be asked to create a GitHub account if you don't already have one.

---

### How can I read this tutorial without an Internet connection? <img alt="GIF" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/hmm.gif" width="20vw" />

1. Go [**`here`**](https://github.com/A-Alexander-code/IA-Projects) and click the big green ➞ **`Code`** button in the top right of the page, then click ➞ [**`Download ZIP`**](https://github.com/A-Alexander-code/IA-Projects/archive/refs/heads/main.zip).

    ![Download ZIP](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/Captura%20de%20pantalla%202024-04-25%20132018.png)

2. Extract the ZIP and open it. Unfortunately I don't have any more specific instructions because how exactly this is done depends on which operating system you run.
    
3. Launch ipython notebook from the folder which contains the notebooks. Open each one of them
  
    `Kernel > Restart & Clear Output`
    
This will clear all the outputs and now you can understand each statement and learn interactively.

If you have git and you know how to use it, you can also clone the repository instead of downloading a zip and extracting it. An advantage with doing it this way is that you don't need to download the whole tutorial again to get the latest version of it, all you need to do is to pull with git and run ipython notebook again.

---

## Authors ✍️

I'm Msc. Alexander and I have written this tutorial. If you think you can add/correct/edit and enhance this tutorial you are most welcome🙏

See [github's contributors page](https://github.com/A-Alexander-code/IA-Projects/graphs/contributors) for details.

If you have trouble with this tutorial please tell me about it by [Create an issue on GitHub](https://github.com/A-Alexander-code/IA-Projects/issues/new). and I'll make this tutorial better. This is probably the best choice if you had trouble following the tutorial, and something in it should be explained better. You will be asked to create a GitHub account if you don't already have one.

If you like this tutorial, please [give it a ⭐ star](https://github.com/A-Alexander-code/IA-Projects).

---

## Licence 📜

You may use this tutorial freely at your own risk. See [LICENSE](https://github.com/A-Alexander-code/IA-Projects/blob/main/LICENSE).

Copyright (c) 2024 Msc. Alexander P.

---

<div align="center">
<h3> Connect with me<a href="https://gifyu.com/image/Zy2f"><img src="https://github.com/milaan9/milaan9/blob/main/Handshake.gif" width="50px"></a>
</h3> 
<p align="center">
    <a href="https://www.linkedin.com/in/bryan-peralta-6049a8198" target="_blank"><img alt="LinkedIn" width="25px" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Linkedin.svg"></a>
    <a href="alexander:b_alx_arboleda@outlook.com" target="_blank"><img alt="Gmail" width="25px" src="https://upload.wikimedia.org/wikipedia/commons/d/df/Microsoft_Office_Outlook_%282018%E2%80%93present%29.svg"></a> 