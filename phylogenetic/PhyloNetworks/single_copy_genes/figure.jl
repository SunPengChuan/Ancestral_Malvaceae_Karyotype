using PhyloNetworks
using PhyloPlots
using RCall
using CSV

R"pdf"("plot-all.pdf")
R"layout(matrix(1:6,3,2,byrow = T))"

R"par"(mar=[0,0,0,0])
net0 = readSnaqNetwork("net0.out")
net1 = readSnaqNetwork("net1.out")
net2 = readSnaqNetwork("net2.out")
net3 = readSnaqNetwork("net3.out")
net4 = readSnaqNetwork("net4.out")
net5 = readSnaqNetwork("net5.out")
net6 = readSnaqNetwork("net6.out")
plot(net0, :R,showGamma=true)
plot(net1, :R,showGamma=true)
plot(net2, :R,showGamma=true)
plot(net3, :R,showGamma=true)
plot(net4, :R,showGamma=true)
plot(net5, :R,showGamma=true)
R"dev.off()";