import numpy as np
import matplotlib.pyplot as plt

class Displayer():
    def __init__(self):
        pass
    
    def display(self, picture):
        """
        Display rendered picture in a window
        """
        print("shape:" + str(picture.shape))
        picture = np.uint8(picture)
        plt.imshow(picture)
        
        plt.show()
        pass