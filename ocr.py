# ocr.py

import pdfplumber
import pytesseract
from PIL import Image


def extract_text(file_path):

    text = ""

    if file_path.lower().endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text

    else:

        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)

    return text