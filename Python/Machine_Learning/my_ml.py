import numpy as np
import pandas as pd
import matplotlib


df = pd.read_csv(r'C:\MLCourse\PastHires.csv')
#print (df.columns)
#print(df[['Previous employers','Hired']][:5])

level = df['Level of Education'].value_counts()
print level
print level.plot(kind='bar')