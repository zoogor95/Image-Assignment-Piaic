import os
from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow




def main():
  gfile=os.getcwd()+"\\"+"*.jpg"
  new_width  = 200
  new_height = 200
  size=(new_width, new_height)
  new_RGB=3
  imageArray = np.empty([20,200,200,3], dtype = int)
  fileList = glob.glob(gfile)
  index=0
  print()
  for f in fileList:
    image = Image.open(f)
      
    image=image.resize(size)
      
    imageArray[index]=image
    plt.figure()
    plt.imshow(image)
    index=index+1

if __name__ == "__main__":
    main()