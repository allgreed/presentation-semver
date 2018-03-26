"""
Produced by SPAM inc.
All right reserved

Version: 1.0.0
"""

from functools import reduce
from operator import add

def sum(iterable):
    return reduce(add, iterable)
    
# divide
