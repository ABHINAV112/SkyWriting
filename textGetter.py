import io
import os

def detect_text(path):
    text_list=''
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if(len(texts)!=0):
        text_list=texts[0].description.replace('\n', ' ')
        return(text_list)

    else:
        return('')


if(__name__=="__main__"):

    testText = detect_text("output/temp.png")
    print(testText)