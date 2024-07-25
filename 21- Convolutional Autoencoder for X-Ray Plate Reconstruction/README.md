<p align="center"> 
<a href="https://github.com/A-Alexander-code"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=A-Alexander-code&color=ff3300" alt="Last Commit"/></a> 
</p> 
<!--<img src="https://badges.pufler.dev/contributors/milaan9/01_Python_Introduction?size=50&padding=5&bots=true" alt="milaan9"/>-->

# Convlutional Autoencoder for Chest X-Ray Image Reconstruction

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/20111107-lung.jpg)

This project focuses on building, training, and evaluating a Convolutional Autoencoder (CAE) using TensorFlow and Keras. The goal of the CAE is to learn a compressed representation (encoding) of chest X-ray images and then reconstruct them as accurately as possible.

## Background

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/The-convolutional-autoencoder-structure.png)

A Convolutional Autoencoder (CAE) is a type of neural network designed for unsupervised learning tasks, specifically for image data. It combines convolutional neural networks (CNNs) with autoencoders. 

- **Encoder**: The encoder part of the CAE compresses the input image into a lower-dimensional latent representation by applying a series of convolutional layers. This process captures essential features and patterns from the input data.

- **Decoder**: The decoder then reconstructs the original image from this compressed representation using convolutional transpose layers (also known as deconvolution layers). The goal is to produce an output as similar as possible to the original input.

The CAE is trained to minimize the difference between the input and the reconstructed output, effectively learning to capture and reconstruct important features of the image data. This makes CAEs useful for tasks like image denoising, anomaly detection, and feature learning.

## Project Structure

### Main Files

1. `convolutional_autoencoder.py`
2. `my_data_generator.py`
3. `training_CAE.ipynb`
4. `utils.py` 

### File Descriptions

#### `convolutional_autoencoder.py`

This file defines the `ConvAutoencoder` class, which encapsulates the construction, compilation, and training of the CAE model. Key methods include:

- `__init__`: Initializes model parameters.
- `build`: Constructs the model architecture.
- `compile`: Compiles the model with an optimizer and loss function.
- `train`: Trains the model using data generators and callbacks.
- `save_model`: Saves the trained model and its configuration.
- `load_model`: Loads a previously trained model.
- `plot_model`: Generates and saves diagrams of the model architecture.

#### `my_data_generator.py`

Defines the `DataGenerator` class, inheriting from `tf.keras.utils.Sequence` to generate batches of data for model training. Key methods include:

- `__init__`: Initializes generator parameters.
- `__len__`: Computes the number of batches per epoch.
- `on_epoch_end`: Shuffles data indices at the end of each epoch if `shuffle` is `True`.
- `__getitem__`: Generates a batch of data.
- `get_sample`: Loads and preprocesses an image from disk.
- `norm`: Normalizes images.

#### `training_CAE.ipynb`

This Jupyter Notebook is used to train and evaluate the CAE model. Major sections include:

1. **Library Imports**: Imports necessary libraries.
2. **Hyperparameters Definition**: Sets model and training parameters.
3. **I/O Paths Configuration**: Defines paths for data, models, and results.
4. **Directory Structure Creation**: Creates necessary directories.
5. **Hyperparameters Saving**: Saves hyperparameters to a JSON file.
6. **Training Phase**: Loads training and validation data, builds, and trains the model.
7. **Model Evaluation**: Loads test data, makes predictions with the trained model.
8. **Saving Reconstructed Images**: Saves reconstructed images for analysis.

## Results

### Training Graphs

- **Training and Validation Loss**: Visualize the loss curves during training and validation. These plots show how the model's performance improved over epochs.

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/training_loss.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After fifty epochs of training, the CAE model achieved a loss of 0.0029 and a validation loss of 0.0048.

### Reconstructed Images

- **Original vs. Reconstructed**: Compare original chest X-ray images with their reconstructions to assess the quality of the model’s output. The first image in the 'Original' section shows one of the images used for training the model. The second image displays the reconstructed image (left) and the original image (right).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original:<br/>
![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/x_ray_chest_original.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reconstructions using CAE:<br/>
![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/image_0.png)

### Model Architecture Diagrams

- **Model Summary**: Diagrams of the CAE architecture, including the encoder and decoder networks, showing layer configurations and data flow.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Decoder architecture:<br/>
![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/modelDecoder.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Encoder architecture:<br/>
![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/modelEncoder.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convlutional Autoencoder architecture:<br/>
![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/modelCAE.png)

## Usage

1. **Prepare Data**: Place your images in the folder specified by `run_folders["data_path"]`.
2. **Configure Hyperparameters**: Adjust parameters in `training_CAE.ipynb` as needed.
3. **Train the Model**: Run the cells in `training_CAE.ipynb` to train the model.
4. **Evaluate the Model**: Use provided cells to evaluate the model's performance and save results.

_Note_: Due to confidentiality issues, the images used for training this model cannot be shared.

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
