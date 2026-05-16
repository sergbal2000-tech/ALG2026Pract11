import os
from PIL import Image

Dir = "IM"
tip = ('.jpg', '.png')

for i in os.listdir(Dir):
    if i.lower().endswith(tip):
        im = os.path.join(Dir, i)
        try:
            img = Image.open(im)
            print("Файл:", i)
            print("Размер: ", img.size)
            print("Формат: ", img.format)
            print("Цветовая модель: ", img.mode)
            print("")
        except Exception as e:
            print(f"Ошибка при открытии {i}: {e}")