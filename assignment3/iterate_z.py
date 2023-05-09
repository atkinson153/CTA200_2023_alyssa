import numpy as np
def iterate(c_arr, index):
    """iterate the mandelbrot map
    
    Inputs:
    c_arr------array-like, coordinates of a pt in the complex plane 
    
    index----number of iterations
    
    Returns:
    Iteration at which the point is beyond the critcal limit
    """
    
    z=0
    for i in range(index):
        z = z*z +c_arr
    return np.isnan(abs(z))==False, np.isnan(abs(z))== True #boolean numpy arrays 

