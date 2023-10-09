#!/usr/bin/env julia

using Distributed
nruns = 15
addprocs(nruns)
@everywhere using PhyloNetworks

starting_tree = readTopology("start.tre");
using DataFrames, CSV
df_sp = DataFrame(CSV.File("tableCF.csv", pool=false); copycols=false);
d_sp = readTableCF!(df_sp);
net0 = snaq!(starting_tree, d_sp, hmax=0, filename="net0", seed=1234,runs=15)
net1 = snaq!(net0, d_sp, hmax=1, filename="net1", seed=1234,runs=15)
net2 = snaq!(net1, d_sp, hmax=2, filename="net2", seed=1234,runs=15)
net3 = snaq!(net2, d_sp, hmax=3, filename="net3", seed=1234,runs=15)
net4 = snaq!(net3, d_sp, hmax=4, filename="net4", seed=1234,runs=15)
net5 = snaq!(net4, d_sp, hmax=5, filename="net5", seed=1234,runs=15)
net6 = snaq!(net5, d_sp, hmax=6, filename="net6", seed=1234,runs=15)
