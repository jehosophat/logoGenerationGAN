import cv2
import os
from matplotlib import pyplot as plt
from PIL import Image

def main():
    save_dir_file_canny = os.getcwd() + os.sep + "demo_canny"
    save_dir_file_sobel = os.getcwd() + os.sep + "demo_sobel"
    save_dir_file_laplacian = os.getcwd() + os.sep + "demo_laplacian"
    os.chdir("./demo_data")
    image_names = os.listdir()
    for image_name in image_names:
        img = cv2.imread(image_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=7)
        laplacian_img = cv2.Laplacian(img, ksize=3, ddepth=cv2.CV_16S)
        #cv2.imwrite(save_dir_file+os.sep+image_name, edges)
        #cv2.imwrite(save_dir_file_sobel+os.sep+image_name, sobelxy)
        #cv2.imwrite(save_dir_file_laplacian+os.sep+image_name, laplacian_img)

    return


def plot_images():
    fig = plt.figure(figsize=(10,10))
    os.chdir("./demo_sobel")
    image_names = os.listdir()    
    for i in range(5):
        for j in range(5):
            index = i*5+j
            fig.add_subplot(5,5, index+1)
            #img = cv2.imread(image_names[index], cv2.IMREAD_GRAYSCALE)
            img = Image.open(image_names[index])
            plt.imshow(img, cmap='gray')
            plt.axis('off')

    
    plt.show()


    return

plot_images()

#main()