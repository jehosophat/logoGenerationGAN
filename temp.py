import random
import os

def main():

    cur_dir = os.getcwd()
    os.chdir(cur_dir+os.sep+"data"+os.sep+"LLD-logo-files")
    file_names = os.listdir()
    print(len(file_names))
    randomlist = []
    for i in range(0,25):
        n = random.randint(0,len(file_names))
        randomlist.append(n)
    for j in randomlist:
        print(os.getcwd()+os.sep+file_names[j])
        os.system("copy " + os.getcwd()+os.sep+file_names[j] + " C:\\Users\\LEOPARD\\logoGAN\\logoGenerationGAN\\demo_data"+os.sep+file_names[j])


    return


main()