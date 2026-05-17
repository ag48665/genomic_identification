# Computational Methods for Human Identification from Degraded and Mixed DNA Samples
## Using Deep Learning and Probabilistic Genomic Inference

This project develops a computational genomics framework for human identification from degraded and mixed DNA samples using 1000 Genomes Project genotype data.

## Overview

Forensic DNA samples are often degraded, incomplete, or composed of DNA from multiple individuals. This project simulates these conditions and evaluates how genomic identity matching performs under increasing uncertainty.

## Dataset

- 1000 Genomes Project Phase 3
- Chromosome 20 genotype VCF
- 2,504 individuals
- Subset used for MVP: 10,000 SNPs × 100 individuals

## Methods

- Genotype matrix extraction from VCF files
- Synthetic DNA degradation via SNP dropout
- Mixed DNA sample simulation
- Cosine-similarity identity matching
- Entropy-based uncertainty estimation
- PCA visualization of genomic mixture space
- Deep neural network baseline for genomic embeddings

## Key Results

- Identification remained robust up to 50% SNP dropout.
- Accuracy dropped sharply at 70–90% degradation.
- Balanced 50/50 DNA mixtures showed the highest uncertainty.
- Dominant-contributor mixtures produced lower entropy and higher confidence.
- Deep learning models learned genomic embeddings but showed overfitting under limited identity-level supervision.

## Figures

![Degradation Accuracy](figures/degradation_accuracy_curve.png)

![Mixture Entropy](figures/mixture_balance_vs_entropy.png)

![PCA Mixed Samples](figures/pca_mixed_samples.png)

![Deep Embedding Space](figures/deep_genomic_embedding_space.png)

## Project Structure

```text
data/
notebooks/
figures/
results/
src/
README.md
requirements.txt
