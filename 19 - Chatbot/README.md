<p align="center"> 
<a href="https://github.com/A-Alexander-code"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=A-Alexander-code&color=ff3300" alt="Last Commit"/></a> 
</p> 


# Create Chatbot with Python & Artificial Intelligence

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/chatbot_project.png)

Do you want your friend to solve your problems instantly? And most importantly, do you want your friend to be with you for the rest of your life? Then you don’t have to be worried. All of these qualities may be found in the most widely used AI application, the CHATBOT!

## What is Chatbot?

A chatbot is a software application that uses artificial intelligence and natural language processing to allow you to have a text-based or text-to-speech conversation.

## Types of Chatbots:

1. **Rule-based Chatbots**: Rule-based chatbots are often known as decision tree bots since they understand queries using a tree-like flow. For each query, it has a set of predefined responses. They aren’t aware of the context of the user’s query.

2. **AI-based Chatbots**: AI chatbots use natural language processing (NLP) and machine learning to understand the context and intent of a user’s query pattern and to create connections between different queries which are asked in different ways in order to provide a better response.

## About the Python Chatbot Project:

In this Chatbot project, we are going to make an AI-based contextual chatbot that will maintain the context or sense in which the user is asking a query. Using deep learning techniques in Python, we will construct a Sequential model for our training sets of data. The intents, patterns, and responses will all be used to train the chatbot. The user’s query will be mapped to the intents class using neural networks, which will maintain context and then return a random response.


## How to Create a Chatbot in Python?

Before creating the chatbot, let’s have a glance through the project file structure.

### Python Chatbot Files:

- **intents.json**: This file contains sets of tags, patterns, and responses. The intent of every class has a set and filter to check in which contexts the user query belongs to.
- **training.py**: This file is used to create the model and train our Python chatbot.
- **training_data.file**: This file contains lists of words, patterns, and training sets in a binary format which we get when we train our chatbot model.
- **chatbot_model.h5**: This file stores the trained model neurons' weights and the configuration of the model.
- **testing.py**: This file is used to predict in which tag (classes) the user’s query belongs to and return a random response from that tag.
- **chatbot_gui.py**: This file is the GUI for the Chatbot where users can interact with the bot and also train their bot.

### Steps to Create the Chatbot:

1. **Import modules and load intents file**:
   - Create a file named `training.py` and import all required modules.
   - Create a class with the name “Training”. In the constructor of this class, initialize all variables accessible through all class methods. Read the `intents.json` file and parse it into the ‘intents’ variable. 

2. **Preprocessing the Data**:
   - Tokenize the data to split the text into words.
   - Create a document variable to hold tokenized words and their respective tag or class name.
   - Perform lemmatization to reduce words to their root form and remove symbols, and convert all words to lowercase.

3. **Bag of Words and Training Sets**:
   - Use the Bag of Words model to one-hot encode the textual data into numerical data.
   - Create training sets containing input patterns and output classes.
   - Shuffle the training sets to avoid overfitting.

4. **Build the Machine Learning Model**:
   - Use the training sets to build a Sequential model with three layers: input layer, hidden layer, and output layer.
   - Train the model and save it along with the words and classes.

5. **Predicting the Response for User’s Query**:
   - Create a `testing.py` file to load the trained model and predict the class for user queries.
   - Perform lemmatization and vectorization on user input and use the model to predict the tag.
   - Maintain context for follow-up queries and return appropriate responses.

6. **Creating a GUI for the Chatbot**:
   - Use Python’s Tkinter module to create a graphical user interface.
   - Create the main window, text area for displaying conversation, and input entry for user queries along with a Send button.
   - Implement event handling for the Send button to display user queries and bot responses.
   - Provide an interface for training the chatbot with new intents.

With these steps, you can create a contextual AI-based chatbot using Python and deep learning techniques. This chatbot can handle user queries, maintain context, and be trained with new data to improve its responses.


---


## Install Necessary Modules:

Open your [![Anaconda](https://img.shields.io/badge/Anaconda-342B029.svg?&style=flate&logo=anaconda&logoColor=white)](https://www.anaconda.com/products/individual) Prompt <img alt="propmt" src="https://img.shields.io/badge/-__-000000?style=flat-square&logo=Plex&logoColor=white"> and type and run the following command (individually):

- **Python**: 3.8.5
- **Tensorflow**: 2.13.0 (Note: TensorFlow version should be 2.2 or higher in order to use Keras or else install Keras directly)
- **sklearn**: 1.5.0
- **pickle**: 4.0
- **numpy**: 1.24.3
- **nltk**: 3.8.1

### How to use requirements.txt to install dependencies:

To replicate the development environment on another machine or environment, you can use the requirements.txt file with the following command:

 -       pip install -r requirements.txt


Once Installed now we can import it inside our python code.

---

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
