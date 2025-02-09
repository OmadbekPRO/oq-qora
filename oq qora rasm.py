# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U5PMgBVT37pd3ZYHOtNOjtZp2LPo5IXm
"""

# Pillow kutubxonasini o'rnatish
!pip install Pillow

from PIL import Image
import matplotlib.pyplot as plt

# Rasm yuklash va oq-qora tasvirga aylantirish funksiyasi
def convert_to_grayscale(image_path):
    # Rasmni ochish
    img = Image.open(image_path)
    # Oq-qora tasvirga aylantirish
    grayscale_img = img.convert('L')
    # Yangi tasvirni saqlash
    grayscale_img.save('grayscale_' + image_path)

    return grayscale_img

# 1-rasm uchun
image_path1 = '1.jpg'  # Rasm yo'lini belgilang
grayscale_img1 = convert_to_grayscale(image_path1)

# 2-rasm uchun
image_path2 = '2.jpg'  # Rasm yo'lini belgilang
grayscale_img2 = convert_to_grayscale(image_path2)

# 3-rasm uchun
image_path3 = '3.jpg'  # Rasm yo'lini belgilang
grayscale_img3 = convert_to_grayscale(image_path3)

# Tasvirlarni ko'rsatish
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(grayscale_img1, cmap='gray')
plt.title('1-rasm Oq-Qora')

plt.subplot(1, 3, 2)
plt.imshow(grayscale_img2, cmap='gray')
plt.title('2-rasm Oq-Qora')

plt.subplot(1, 3, 3)
plt.imshow(grayscale_img3, cmap='gray')
plt.title('3-rasm Oq-Qora')

plt.show()