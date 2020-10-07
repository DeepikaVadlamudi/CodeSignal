import numpy as np
def rotateImage(a):
    a = np.rot90(np.array(a),k=3)
    return a
            
