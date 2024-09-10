<p align="center"> 
<a href="https://github.com/A-Alexander-code"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=A-Alexander-code&color=ff3300" alt="Last Commit"/></a> 
</p> 
<!--<img src="https://badges.pufler.dev/contributors/milaan9/01_Python_Introduction?size=50&padding=5&bots=true" alt="milaan9"/>-->

# Face Recognition Project

![image](https://github.com/A-Alexander-code/IA-Projects/blob/main/z_image/face_recognition.gif)

This project implements a simple face recognition system using Python and OpenCV. It consists of three main scripts:

1. **`face_taker.py`**: Captures face images from the webcam and stores them in a directory.
2. **`face_train.py`**: Trains a face recognition model using the captured face images.
3. **`face_recognizer.py`**: Recognizes faces using the trained model and displays the results in real-time.

### 1. Install the required packages:

    pip install numpy pygame opencv-python pillow

### 2. Download the Haar Cascade file for face detection:

You can download the `haarcascade_frontalface_default.xml` file from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.

### 3. Prepare sound files:

Place your sound files in a directory named `Sound` within the project directory. The files should be named `Message Notification 01.mp3` and `Message Notification 02.mp3` or modify the paths in the face_taker.py script.

## **Usage**

### 1. Face Capture

Run `face_taker.py` to capture face images and store them in the images directory. This script will prompt you to enter a username, which will be associated with the captured images.

    python face_taker.py

### 2. Train the Model

Run `face_train.py` to train the face recognition model using the images captured in the previous step. The trained model will be saved as `trainer.yml`.

    python face_train.py

### 3. Face Recognition

Run `face_recognizer.py` to recognize faces in real-time using your webcam. The script will display the recognized name and confidence level on the screen.

    python face_recognizer.py

## **Project Structure**

    face-recognition/
    │
    ├── face_taker.py           # Captures and saves face images
    ├── face_train.py           # Trains the face recognition model
    ├── face_recognizer.py      # Recognizes faces in real-time
    ├── haarcascade_frontalface_default.xml  # Haar Cascade file for face detection
    ├── trainer.yml             # Trained model (generated after running face_train.py)
    ├── names.json              # JSON file to map user IDs to names
    └── images/                 # Directory containing captured face images

## How It works

1. **Face Capture**: The `face_taker.py` script captures images from your webcam, detects faces, and saves them in the `images` directory with a unique identifier.

2. **Training**: The `face_train.py` script loads the images, extracts face regions, and trains a model using the Local Binary Patterns Histograms (LBPH) algorithm. The trained model is saved as `trainer.yml`.

3. **Recognition**: The `face_recognizer.py` script uses the trained model to recognize faces in real-time. It compares the captured face with the trained faces and displays the name and confidence level.

## Requirements

* Python 3.x
* OpenCV
* Pygame
* NumPy
* Pillow


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