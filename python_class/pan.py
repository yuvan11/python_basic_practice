import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

DATA={
     'stud name':["priya","sowmya","roshini","raji","rasi"],
     'EMID':[10013,10025,10035,10045,10056],
     'STUT_PERCENTAGE':[78,80,65,74,75],
     'STUT_PREV_PERCENTAGE':[85,75,80,65,90],
     'EMYEAR':["1/2/2015","1/1/2015","1/1/2016","2/3/2016","1/1/2016"],
     'PLACE':["MARTHANDAM","TIRUNALVELI","KANAYAKUMARI","TIRUCHI","COIMBATORE"],
     'CORE':["SOFTWARE","SOFTWARE","DATASCIENTIST","AI","SOFTWARE"]
    }

data={'marks':[10,20,30,40,50],
      'marks_1':[20,30,40,50,60],
'stud name':["priya","sowmya","roshini","raji","rasi"],
      }

df = pd.DataFrame(DATA)
print(df)
df1=pd.DataFrame(data)
merge_option=pd.merge
print(merge_option)
print(df.columns)
print(df['EMID'])
print(df.EMID)
print(df[['CORE','EMID']])

# show head data
print(df.head())
# # show tail data
print(df.tail(1))
# # show data values
print(df.values)
# # sum of data
print(df.sum())
# # mean value
print(df.mean())
print(df.info())
