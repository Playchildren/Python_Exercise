# import
import math
print(math.sqrt(9))


# from xx import xx
from math import sqrt
print(sqrt(9))

from random import randint
print(randint(1, 9))


# from xx import*
from math import *
print(sqrt(9))

"""
定义别名
"""
import math as my
from random import randint as rdt
print(my.sqrt(rdt(1, 9)))

import time as tt
tt.sleep(2)
print('hello')