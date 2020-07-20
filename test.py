# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:52:38 2020

@author: HT
"""

import numpy as np
import scipy.integrate as integrate
norms = lambda x: np.exp(-x**2/2.0)/np.sqrt(2.0*3.14159)
i, e = integrate.quad(norms, -np.inf, np.inf)

print('Integral : '+str(i))
print('Absolute Error: '+str(e))