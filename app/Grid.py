from Pixel import Pixel
from PIL import Image
import numpy as np

class Grid:
    def __init__(self, x_lim, y_lim, path):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.array=[]
        self.path=path
        for i in range(x_lim):
            for j in range(y_lim):
                self.array.append(Pixel(i,j))

    def printArray(self):
        print(self.array)

    def update(self, x, y, value):
        for p in (p1 for p1 in self.array if p1.x==int(x) and p1.y==int(y)):
            p.value=((value=='True') or value)
            break
        self.saveImage()

    def saveImage(self):
        im_array = [[False for x in range(self.x_lim)] for y in range(self.y_lim)]
        for p in self.array:
            if p.value==True:
                im_array[p.x][p.y]=p.value
        c_array = np.asarray(im_array)
        image = Image.fromarray(c_array)
        image.save(self.path)