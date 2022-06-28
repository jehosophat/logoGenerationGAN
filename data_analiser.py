import numpy as np
import os
from matplotlib import pyplot as plt
from PIL import Image




def main():

    os.chdir(os.getcwd() + os.sep + "data"+ os.sep + "LLD-logo-files")
    image_names = os.listdir()
    print(len(image_names))
    width_arrray = []
    height_array = []

    for i in range(100):
        print(i)
        if i == 99:
            for j in range(1312):
                image_name = image_names[i*1222+j]
                img = Image.open(image_name)
                img_array = np.asarray(img)
                x, y, _ = img_array.shape
                width_arrray.append(x)
                height_array.append(y)
        else:
            for j in range(1222):
                image_name = image_names[i*1222+j]
                img = Image.open(image_name)
                img_array = np.asarray(img)
                x, y, _ = img_array.shape
                width_arrray.append(x)
                height_array.append(y)

    print(len(width_arrray))
    print(len(height_array))
    
    print(min(width_arrray))
    print(min(height_array))
    print(max(width_arrray))
    print(max(height_array))

main()

#resim boyutları için matplotlib grafiği çıkar