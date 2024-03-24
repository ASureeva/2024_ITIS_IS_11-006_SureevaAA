import pandas as pd

#
# df = pd.DataFrame({'Words': [0, 0, 0, 0, 0, 0],
#                    'TF': [0, 0, 0, 0, 0, 0],
#                    'IDF': [176000000, 188500000, 90000000,
#                                       100000000, 180500000, 105000000],
#                    'list_column': [[1, 2, 0, 0, 0, 0], [3, 4, 0, 0, 0, 0], [5, 6, 0, 0, 0, 0]]
#                    })

df = pd.DataFrame({'list_column': [[1, 2], [3, 4], [5, 6]]})
df_expanded = pd.DataFrame(df['list_column'].tolist(), index=df.index)
df.to_excel('./teams.xlsx')