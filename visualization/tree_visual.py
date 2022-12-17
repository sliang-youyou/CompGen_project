from Bio import Phylo

tree = Phylo.read('tree_visualize.nwk', 'newick')

# Phylo.draw(tree, branch_labels=lambda c: c.branch_length)
Phylo.draw(tree)
