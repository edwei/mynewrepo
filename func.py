import pandas as pd
import numpy as np
import matplotlib as plt
%matplotlib inline

print('\n'.join('\t'.join("%dx%d=%d" % (x, y, x*y) for x in range(1, 10)) for y in range(1, 10)))
