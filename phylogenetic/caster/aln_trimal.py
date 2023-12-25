import numpy as np
import pandas as pd
import wgdi.base as base
import os
import sys
import shutil
from Bio import AlignIO, Seq, SeqIO, SeqRecord

alignment_file = sys.argv[1]
cds_file = sys.argv[2]
dir_path = sys.argv[3]
trimal_files = sys.argv[4]

minimum=4

alignment = pd.read_csv(alignment_file, header=None)
alignment.replace('.', np.nan, inplace=True)
alignment.dropna(thresh=int(minimum), inplace=True)

data =[]
seq_cds = SeqIO.to_dict(SeqIO.parse(cds_file, "fasta"))
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
for index, row in alignment.iterrows():
    file = base.gen_md5_id(str(row.values))
    sequencefile = os.path.join(dir_path, file+'.fasta')
    alignfile = os.path.join(dir_path, file+'.aln')
    align_trimming = alignfile+'.trimming'
    if os.path.isfile(align_trimming):
        data.append(align_trimming)
        continue
    print(alignfile)
    ids_cds = []
    for i in range(len(row)):
        if type(row[i]) == float and np.isnan(row[i]):
            continue
        gene_cds = seq_cds[row[i]]
        gene_cds.id = str(int(i)+1)
        ids_cds.append(gene_cds)
    SeqIO.write(ids_cds, sequencefile, "fasta")
    # run muslce
    args = ['muscle', '-in', sequencefile,'-out',alignfile,'-quiet']
    command = ' '.join([str(k) for k in args])
    os.system(command)
    
    #run trimal
    args = ['trimal', '-in', alignfile,'-out',align_trimming,'-automated1','-phylip_paml']
    command = ' '.join([str(k) for k in args])
    os.system(command)

for i in range(0, len(data), 100):
    trees = ' '.join([str(k) for k in data[i:i+100]])
    args = ['cat', trees, '>>', trimal_files]
    command = ' '.join([str(k) for k in args])
    os.system(command)