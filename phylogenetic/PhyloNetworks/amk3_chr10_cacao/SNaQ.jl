#!/usr/bin/env julia

using PhyloNetworks
using PhyloPlots
using CSV

genetrees = readMultiTopology("amk3.tree");
q,t = countquartetsintrees(genetrees);
df = writeTableCF(q,t) 
CSV.write("tableCF.csv", df);