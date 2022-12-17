# CompGen_project
Phylogenetic Analysis of Monkeypox Lineage found in U.S.A. 2021-2022

This project focuses on studying the site-level selection of the Monkeypox genes related to virulence and transmissibility. The following computational pipeline is available for replication and further research.
Involved datasets and softwares should be found in folders named after sections.

# data source
We collected 29 MPXV genome sequences noted in the original paper(*Gigante et al., 2022*).
The reference genome MT903344.1 is in ```ref_seq.fasta```. The other 28 sequences can be found in
```non_ref_seq.fasta```. All sequences are merged in ```sequences_nucleotides.fasta```.
As an alternative, ```accession.txt``` can be used to accessed genomes from
[NCBI MPXV data hub](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?VirusLineage_ss=Monkeypox%20virus%20(monkeypox),%20taxid:10244&HostLineage_ss=humans,%20taxid:9605&SeqType_s=Nucleotide) directly. 

# Multiple Sequence Alignment
[MAFFT](https://mafft.cbrc.jp/alignment/software/) is a free software that performs multiple sequence alignment
using Fast Fourier Transform. The download and installation system depends on your Operating System.
To run the program with iterative refine method, you can run ```mafft --maxiterate 2 "sequences_nucleotides.fasta" > "fftnsi.fasta"``` in the terminal. The output should be the aligned sequences.

# Rid of columns with gaps
[trimAL](http://trimal.cgenomics.org/trimal) filters out any column that contains gaps in the multiple sequence alignment. Command: ```   trimal -in fftnsi.fasta -out fftnsi_nogaps.fasta -nogaps ```.

# Phylogeny Tree Construction
[IQ-tree](http://www.iqtree.org/) constructs the maximum likelihood tree from MSA. Command: ```iqtree -s fftnsi_nogaps.fasta -m K3Pu+F+I```
Then we add the mid-point root to the tree ```fftnsi_rn.treefile``` with R package ```phytools``` and ```ape```.

# Gene set Preparation
Again, we extracted genes from [NCBI](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?VirusLineage_ss=Monkeypox%20virus%20(monkeypox),%20taxid:10244&HostLineage_ss=humans,%20taxid:9605&SeqType_s=Nucleotide). Run them through MAFFT if they are of different length. Use Hyphy command line data file tools to replace inner stop codons with indels. Both raw reverse complement formats and the cleaned data are in the folder. For example, ```MPXVgp003.fasta``` includes the gene ```gp003``` sequence from 29 cases. ```gp003_rev.fasta``` has the corrected data for comparative sequence analysis.

# Hyphy
First download and install software [Hyphy](http://www.hyphy.org/register/) before using it in terminals.

SLAC: 
* Genetic Code: 1 [Universal]
* the number of samples used to assess ancestral reconstruction uncertainty: 100
* p-value threshold to use when testing for selection: 0.1

FEL:
* the set of branches to test for selection: 1[**All**]
* synonymous rate variation?: 1[**Yes**]
* p-value threshold to use when testing for selection: 0.1

MEME:
* the set of branches to test for selection: 1[**All**]
* p-value threshold to use when testing for selection: 0.1
* Perform parametric bootstrap resampling to derive site-level null LRT distributions up to this many replicates per site: 50
* Reduce zero-length branches: 3[**No**]
* Perform branch length re-optimization under the full codon model: 1[**Yes**]

*If encounter any choice of parameters not mentioned here, choose the default values*

Thank you for reading through our methods. We look forward to your suggestions on our project.