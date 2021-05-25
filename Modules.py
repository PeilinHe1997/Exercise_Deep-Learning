#Modules

'''Module in Python
1.Library containing related functionality
2.Can contain submodules, classes, functions
3.Need to be imported before usage
'''
#download module
'''
download:
windows+R
cmd
pip install packagename

check:
python
import numpy 

'''
#preferred
import os
print(os.listdir("."))#read all file names under the same path

#often seen
from os import listdir
print(listdir("."))

import numpy as np
d = np.ndarray(5)
print(d)



import scipy
import random
import pickle
















