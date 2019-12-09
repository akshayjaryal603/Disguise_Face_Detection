import glob as g
import os
import pandas as pd

lof= g.glob('*.jpg')
df= pd.DataFrame(index=range(len(lof)), columns=['name','type'])
for i in range(len(lof)):
    name= str(lof[i])
    if name.startswith('normal'):
        df.name[i]=name;
        df.type[i]=1;
    else:
        df.name[i]=name;
        df.type[i]=0;

print(df); 
