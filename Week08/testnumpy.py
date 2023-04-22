#testnumpy.py
#testing if numpy.array[1,10] includes 10, or if i need to use [1,11] to ensure that 10 is included

import numpy as np

array = np.array(range(1,11))

print (array)
 # printed [1 2 3 4 5 6 7 8 9], this tells me that i need to use np.array(range(1,11))