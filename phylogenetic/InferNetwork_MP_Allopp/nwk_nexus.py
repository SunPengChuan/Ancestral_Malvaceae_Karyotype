import pandas as pd
import numpy as np
import sys

#python nwk_nexus.py 3.old.nwk

df = pd.read_csv(sys.argv[1],sep='\t',header=None)
print(df)

array=['#NEXUS','BEGIN TREES;']
trees=''
for index, row in df.iterrows():
    text = 'Tree geneTree'+str(index+1)+' = ' +row[0] 
    array.append(text)
    trees +='geneTree'+str(index+1)+','

array.append('END;')

array.append('BEGIN PHYLONET;')

species='< cpa:1; cca:2; tc180:3; hum:4; dz:5,6,7; hli:8,9; opy:10,11,12,13,14; cotton:15,16,17,18,19 >;'
command  = 'InferNetwork_MP_Allopp ('+trees[:-1]+')'+'2 -a '+species+'-pl 12 -di'
array.append(command)

array.append('END;')
# print(array)
data = pd.DataFrame(array)
data.to_csv(sys.argv[2],sep='\t',index=False,header=False)
