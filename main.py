from skyWriting import skyWrite
from autoCorrect import autoCorrect
from textGetter import detect_text

def main():
    skyWrite()
    text = detect_text("output/temp.png")
    print(text)
    text = autoCorrect(text)
    print(text)
    return text 

if(__name__=="__main__"):
    main()