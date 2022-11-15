from pytesseract import pytesseract
from PIL import Image


path_to_pytesseract = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image_path = r"D:\2022_Fall\CS_4775\project\CompGen_project\prep\variants.jpg"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_pytesseract

text = pytesseract.image_to_string(img).splitlines()

output = []

for token in text:
    output.append(token[0: 8]) if len(
        token) >= 8 and token[2: 8].isdigit() else ()

# Check the number of sequences

print(len(output))

# output format
output = '\n'.join(output)
print(output)
