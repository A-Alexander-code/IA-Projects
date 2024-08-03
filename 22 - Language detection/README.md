<p align="center"> 
<a href="https://github.com/A-Alexander-code"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=A-Alexander-code&color=ff3300" alt="Last Commit"/></a> 
</p> 
<!--<img src="https://badges.pufler.dev/contributors/milaan9/01_Python_Introduction?size=50&padding=5&bots=true" alt="milaan9"/>-->

# Language Detection, Claim Identification, and Sentiment Analysis Project

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/Sentiment-Analysis.png)

In today's globalized world, the ability to understand and process multiple languages is more important than ever. This project aims to develop a comprehensive Natural Language Processing (NLP) model that not only detects languages but also identifies claims and analyzes sentiment in textual data. Leveraging a diverse dataset comprising 30 languages, this project seeks to advance the capabilities of multilingual text processing.

## Overview

This project involves building a multi-output classification model using TensorFlow and Keras. The model is designed to handle three different tasks:

1. **Claim Classification**: Predicting whether a claim is true or false.
2. **Sentiment Analysis**: Determining the sentiment of a statement (positive, negative, or neutral).
3. **Language Identification**: Identifying the language of a given text.

## Model Architecture

The model is designed with the following components:

1. **Inputs**:
   - Claim Input
   - Sentiment Input
   - Language Input

2. **Layers**:
   - **Embedding Layer**: Uses pre-trained embeddings for better representation.
   - **Bidirectional LSTM Layers**: To capture dependencies in sequences.
   - **Dropout Layers**: For regularization and preventing overfitting.
   - **Dense Layers**: For final classification tasks.

3. **Outputs**:
   - **Claim**: Binary classification (True/False).
   - **Sentiment**: Multi-class classification (Positive/Negative/Neutral).
   - **Language**: Multi-class classification for 30 languages.

## Metrics

The following metrics are used to evaluate the model:

- **Accuracy**
- **F1 Score**
- **Precision**
- **Recall**

## Results

Here are the results of the model evaluation on the test dataset:

- **Claim Classification**:
  - Test Accuracy: 0.76571
  - Test F1 Score: 0.46948
  - Test Precision: 0.66828
  - Test Recall: 0.51491

- **Sentiment Analysis**:
  - Test Accuracy: 0.44
  - Test F1 Score: 0.36282
  - Test Precision: 0.42416
  - Test Recall: 0.39525

- **Language Identification**:
  - Test Accuracy: 0.68747
  - Test F1 Score: 0.63292
  - Test Precision: 0.66561
  - Test Recall: 0.63626

Overall, the model shows promising performance in claim and language classification but needs significant improvement in sentiment classification to achieve a more balanced and accurate performance across all metrics.

## Requirements

- TensorFlow
- Keras
- Pandas
- NumPy
- OpenCV
- PIL (Python Imaging Library)
- scikit-image

## Installation

Use the following command to install the necessary libraries:


    pip install tensorflow pandas numpy opencv-python pillow scikit-image

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
</p> 