import os
from PIL import Image, ImageFilter

Dir = "filt"
os.makedirs(Dir, exist_ok=True)
Dir_res = "IM"

for i in os.listdir(Dir_res):
    a = os.path.join(Dir_res, i)
    if os.path.isfile(a):
        try:
            img = Image.open(a)
            cont = img.filter(ImageFilter.CONTOUR)
            name, tip = os.path.splitext(i)
            filt_f = os.path.join(Dir, f"{name}_cont{tip}")
            cont.save(filt_f)
            print(f"Фильтр применн к: {i}")
        except Exception as e:
            print(f"Не удалось применить фильтр к  {i}: {e}")