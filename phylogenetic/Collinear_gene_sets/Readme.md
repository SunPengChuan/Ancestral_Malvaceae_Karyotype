Here, we introduce the obtained collinear gene sets.

For a detailed guide on Subgenome-aware analyses, please refer to https://github.com/SunPengChuan/wgdi-example/blob/main/phase_subgenomes.md

Below is the correspondence between the abbreviations and the full names of the species in the file names.
mal : AMK
cca301s : White jute
opy300s : Balsa tree 
dz186s : Durian
hum1s : Herrania umbratica
hli2s : Heritiera littoralis
ga198s : Cotton
cpa1s : Papaya



The files *.alignment.pdf and *.alignment.csv correspond to the visualization and gene set of collinear genes, respectively.

Using *Heritiera littoralis* and AMK as an example (hli2s_mal), we demonstrate the acquisition process. The total.conf file within the hli2s_mal folder contains all the parameters for this process.

The command execution sequence is as follows:

```
wgdi -d total.conf  
wgdi -icl total.conf  
wgdi -bi total.conf  
wgdi -c total.conf  
wgdi -bk total.conf  
wgdi -pc total.conf  
wgdi -a total.conf
```

Note: The above commands should be executed in the specified order to ensure proper acquisition and analysis of collinear genes.