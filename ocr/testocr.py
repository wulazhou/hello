#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

# open image
image = Image.open('5.jpeg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)
filename ="ocr/sb.txt"
with open(filename,'w') as file_obj:
    file_obj.write(code)
