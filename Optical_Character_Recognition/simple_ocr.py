import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def img_to_txt():
    img = Image.open("testocr.png")
    text = pytesseract.image_to_string(img)
    print(text)


img_to_txt()