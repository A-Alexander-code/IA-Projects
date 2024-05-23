import nltk, random, json , pickle
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import flatten
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer=WordNetLemmatizer()

class Training:
    def __init__(self):
        # Read and load the intent file
        data_file=open('19 - Chatbot\intents.json').read()
        self.intents=json.loads(data_file)['intents']
        self.ignore_words=list("!@#$%^&*?")
        self.process_data()

    def process_data(self):
        # Fetch patterns and tokenize them into words
        self.pattern=list(map(lambda x: x["patterns"], self.intents))
        self.words=list(map(word_tokenize, flatten(self.pattern)))
        # Fetch classes i.e. tags and store in documents along with tokenized patterns
        self.classes=flatten([[x["tag"]]*len(y) for x, y in zip(self.intents, self.pattern)])
        self.documents=list(map(lambda x, y: (x, y), self.words, self.classes))
        # Lower case and filter all the symbols from words
        self.words=list(map(str.lower, flatten(self.words)))
        self.words=list(filter(lambda x: x not in self.ignore_words, self.words))
        # Lematize the words and sort the class and word lists
        self.words=list(map(lemmatizer.lemmatize, self.words))
        self.words=sorted(list(set(self.words)))
        self.classes=sorted(list(set(self.classes)))
    
    def train_data(self):
        # Initialize and set analyzer=word as we want to vectorize words not characters
        cv=CountVectorizer(tokenizer=lambda txt: txt.split(), analyzer="word", stop_words=None)
        # Create the training sets for model
        training=[]
        for doc in self.documents:
            # Lower case and lemmatize the pattern words
            pattern_words=list(map(str.lower, doc[0]))
            pattern_words=' '.join(list(map(lemmatizer.lemmatize, pattern_words)))
            
            # Train or fit the vectorizer with all words and transform into one-hot encoded vector
            vectorize=cv.fit([' '.join(self.words)])
            word_vector=vectorize.transform([pattern_words]).toarray().tolist()[0]
            
            # Create output for the respective input output size will be equal to total numbers of classes
            output_row=[0]*len(self.classes)
            
            # If the pattern is from current class put q in list else 0
            output_row[self.classes.index(doc[1])]=1
            cvop=cv.fit([' '.join(self.classes)])
            out_p=cvop.transform([doc[1]]).toarray().tolist()[0]
            
            # Store vectorized word list long with its class
            training.append([word_vector, output_row])
        
        # Shuffle training sets to avoid model to train on same data again
        random.shuffle(training)
        training=np.array(training, dtype=object)
        train_x=list(training[:,0]) # patterns
        train_y=list(training[:,1]) # classes
        return train_x, train_y
    
    def build(self):
        # Load the data from train_data function
        train_x, train_y=self.train_data()
        
        # Create a Sequential model with 3 layers
        model=Sequential()
        # Input layer with latent dimension of 128 neurons and ReLU activation function
        model.add(Dense(128, input_shape=(len(train_x[0]), ), activation='relu'))
        model.add(Dropout(0.5))         # Dropout to avoid overfitting
        # Second laye rwith the latent dimensionof 64 neurons
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        # Fully connected outpu layer with softmax activation function
        model.add(Dense(len(train_y[0]), activation='softmax'))
        '''
        Compile the model with Stochastic Gradient Descent with learning rate and 
        nesterov accelerated gradien descent.
        '''
        sgd=SGD(learning_rate=1e-2, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
        # Fit the model with training input and output sets
        hist=model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=10, verbose=1)
        # Save model and words, classes which can be used for prediction
        model.save('19 - Chatbot\chatbot_model.h5', hist)
        pickle.dump({'words':self.words, 'classes':self.classes, 'train_x':train_x, 'train_y':train_y}, open(r"19 - Chatbot\training_data", "wb"))

#train the model
if __name__ == "__main__":
    Training().build()