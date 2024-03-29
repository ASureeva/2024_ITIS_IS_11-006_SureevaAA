# import pandas as pd
#
# #
# # df = pd.DataFrame({'Words': [0, 0, 0, 0, 0, 0],
# #                    'TF': [0, 0, 0, 0, 0, 0],
# #                    'IDF': [176000000, 188500000, 90000000,
# #                                       100000000, 180500000, 105000000],
# #                    'list_column': [[1, 2, 0, 0, 0, 0], [3, 4, 0, 0, 0, 0], [5, 6, 0, 0, 0, 0]]
# #                    })
#
# df = pd.DataFrame({'list_column': [[1, 2], [3, 4], [5, 6]]})
# df_expanded = pd.DataFrame(df['list_column'].tolist(), index=df.index)
# df.to_excel('./teams.xlsx')
import numpy
import math
import pandas as pd

dictionary = ['a', 'brown', 'chased', 'dog', 'fox', 'is', 'jumps', 'lazy', 'over', 'quick', 'the' ]
words = ['brown', 'dog']
# tf_idf = [[0, 0.41, 0],
#           [0.29,  0.29, 0],
#           [0, 0.41, 0],
#           [0.29, 0.29, 0.41],
#           [0.29, 0.29, 0],
#           [0, 0, 0.41],
#           [0.29, 0, 0],
#           [0.29, 0, 0.41],
#           [0.29, 0, 0],
#           [0.29, 0, 0],
#           [0.58, 0.41, 0.41]]

tf_idf = [[0, 0.29, 0, 0.29, 0.29, 0, 0.29, 0.29, 0.29, 0.29, 0.58],
          [0.41, 0.29, 0.41, 0.29, 0.29, 0, 0, 0, 0, 0, 0.41],
          [0, 0, 0, 0.41, 0, 0.41, 0, 0.41, 0, 0, 0.41]]
vector = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(tf_idf)):
    print(vector, tf_idf[i])
    l = numpy.dot(vector, tf_idf[i])
    print(l)
    k = math.sqrt(sum(map(lambda x: x**2, vector)))*math.sqrt(sum(map(lambda x: x**2, tf_idf[i])))
    print(k)
    print(l/k)
