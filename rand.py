import numpy as np
import random
import quandl



'''
rand_float = random.random()

print(rand_float)
rand_int = random.randint(1,10)
print(rand_int)
rand_matrix = np.random.randint(1,6, (4,6))
print(rand_matrix)

'''
'''

from pandas_datareader import data as wb

Apple = wb.DataReader('AAPL', data_source = 'yahoo', start = '1995-1-1')

print(Apple)

'''

my_data01 = quandl.get('FRED/GDP')

my_data01.to_csv(r'C:\Users\infin\OneDrive\Documentos\Python for Finance')
