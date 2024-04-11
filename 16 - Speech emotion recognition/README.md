## Speech Emotion Recognition Project

This project aims to recognize emotions in speech using machine learning techniques. The model is trained on audio data containing speech samples labeled with different emotions. The goal is to accurately classify the emotional content of speech.

### Dataset
The dataset used in this project includes recordings of speech utterances labeled with emotions such as anger, happiness, sadness, and others. It contains samples from multiple speakers and is suitable for training machine learning models for speech emotion recognition.

### Model Training
The model is trained using deep learning techniques, specifically Convolutional Neural Networks (CNNs). The audio data is preprocessed to extract relevant features, such as Mel-Frequency Cepstral Coefficients (MFCCs), which capture the characteristics of the speech signal. These features are then fed into the CNN model for training.

### Evaluation
The trained model is evaluated using various performance metrics, including accuracy score, confusion matrix, and classification report. The accuracy score measures the overall accuracy of the model in predicting the correct emotions. The confusion matrix provides insights into the model's performance for each class of emotions, while the classification report gives detailed statistics such as precision, recall, and F1-score for each class.

### Results
The model achieves promising results, with accuracy scores consistently above 0.40 for all predictions. This indicates that the model is capable of effectively recognizing emotions in speech.

### Usage
To use the trained model for predicting emotions in speech, follow these steps:
1. Load the trained model using the provided code.
2. Preprocess the audio data to extract features, such as MFCCs.
3. Feed the preprocessed features into the model for prediction.
4. Interpret the model's predictions to determine the emotional content of the speech.

### Requirements
To run the code and use the trained model, ensure you have the following dependencies installed:
- Python (version 3.9)
- Required Python libraries (e.g., NumPy, pandas, librosa, scikit-learn, TensorFlow/Keras)


### Credits
This project was developed by A-Alexander-code. It is based on the research and methodologies outlined in various papers and tutorials on speech emotion recognition.