import os
import docx
from pdfminer.high_level import extract_text
from PIL import Image
import pytesseract
import chardet

def extract_text_from_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.docx':
        doc = docx.Document(file_path)
        return ' '.join([para.text for para in doc.paragraphs])
    elif file_extension == '.pdf':
        return extract_text(file_path)
    elif file_extension in ['.jpg', '.jpeg', '.png', '.bmp']:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    else:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)['encoding']
            return raw_data.decode(encoding)
