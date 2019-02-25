# Sky Writing
This web application detects a blue circular object. Following which the path of the object is traced to obtain an image of a letter or word. This is then processed using the Google Vision API to obtain the text in the image.

The text can then be saved to Firestore by a button click. This text is then loaded into a JS application which displays it using augmented reality against a preset surface.

![demo](https://raw.githubusercontent.com/ABHINAV112/SkyWriting/master/output/screenRecord.gif)

## Quick Start:
pip install all the dependancies using command line/terminal :
```
pip install opencv-python
pip install Google Vision API
pip install Tensorflow
pip install Keras
pip install numpy
```
# Clone the repo
```
git clone https://github.com/ABHINAV112/SkyWriting.git
```
# Running the app
```
python app.py
```
## Dependancies:
flask
opencv-python
Google Vision API
Tensorflow
Keras
numpy

## Demo:
1. Writing and Recognizing Text
2. Web App - whole package

## What We Learnt
1. AR
2. Flask
3. Opencv
4. OCR
5. Javascript
