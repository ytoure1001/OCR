import cv2
from pdf2image import convert_from_path
import pytesseract
import numpy as np

# Step 1: Convert PDF to images
pdf_path = '/Users/youssouftoure/Downloads/UC_Bulletion_adheėsion_v1.4 (ESSAIE).pdf'
images = convert_from_path(pdf_path)

# Step 2: Preprocess and extract text from images
def preprocess_image(image):
    processed_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    return processed_image

# Step 3: Recognize text using Tesseract OCR
def recognize_text(image):
    recognized_text = pytesseract.image_to_string(image)
    return recognized_text

# Step 4: Extract text from PDF
def extract_text_from_pdf(images):
    extracted_text = []

    for image in images:
        # Step 2: Preprocess the image
        processed_image = preprocess_image(image)

        # Step 3: Recognize text using Tesseract OCR
        text = recognize_text(processed_image)

        # Append the recognized text to the extracted_text list
        extracted_text.append(text)

    return extracted_text

# Step 5: Process the PDF and extract text
extracted_text = extract_text_from_pdf(images)

# Step 6: Print the extracted text
for page_num, text in enumerate(extracted_text):
    print(f"Page {page_num+1}:\n{text}\n")
