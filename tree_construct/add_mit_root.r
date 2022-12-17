library(phytools)
library(ape)
library(here)
tree_fftnsi <- read.newick(file = "tree_construct//fftnsi_nr.treefile")

tree_fftnsi_wn <- midpoint.root(tree_fftnsi)
write.tree(tree_fftnsi_wn, file = "fftnsi_wn.treefile")
