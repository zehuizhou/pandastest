import pandas as pd
from pandas import Series, DataFrame
import numpy as np


data = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range(start='20200101', end='20200108')
# print(dates.array)
# print(help(dates))
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])


df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

dic = {'a': 123, 'b': 456}
ds = pd.Series(dic)
print(ds)
