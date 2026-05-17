# Computational Methods for Human Identification from Degraded and Mixed DNA Samples

## Using Deep Learning and Probabilistic Genomic Inference

This project develops a computational genomics framework for forensic-style human identification from degraded and mixed DNA samples using large-scale population genotype data from the 1000 Genomes Project.

The goal is to investigate how genomic identity matching behaves under increasing uncertainty, missing data, and contributor mixtures using both classical similarity-based methods and deep learning approaches.

---

# Overview

Forensic DNA samples are frequently incomplete, degraded, noisy, or composed of DNA originating from multiple individuals. These conditions create major computational challenges for reliable human identification.

This project simulates realistic degradation and DNA mixture scenarios and evaluates genomic matching performance under varying uncertainty levels.

The framework combines:

- probabilistic genomic inference,
- cosine-similarity identity matching,
- entropy-based uncertainty estimation,
- PCA-based genomic visualization,
- and deep neural network embedding models.

---

# Dataset

- **1000 Genomes Project Phase 3**
- Chromosome 20 genotype VCF
- 2,504 individuals available
- MVP subset:
  - 10,000 SNPs
  - 100 individuals

---

# Methods

## Genomic Data Processing

- VCF genotype extraction using `scikit-allel`
- SNP matrix generation
- Genotype encoding into numerical genomic vectors

## DNA Degradation Simulation

Synthetic degradation was simulated using random SNP dropout across varying degradation levels:

- 10%
- 30%
- 50%
- 70%
- 90%

Missing SNPs were masked to emulate damaged forensic DNA samples.

## Mixed DNA Sample Simulation

Synthetic DNA mixtures were generated using weighted combinations of genomic profiles from multiple individuals.

Example mixture ratios:

- 50/50
- 70/30
- 90/10

## Identity Matching

- Cosine similarity–based genomic matching
- Top-match identification
- Confidence score estimation
- Entropy-based uncertainty analysis

## Dimensionality Reduction

Principal Component Analysis (PCA) was used to visualize:

- genomic clustering,
- mixed DNA positioning,
- latent genomic structure.

## Deep Learning Baseline

A neural network classifier was implemented in PyTorch to learn genomic embeddings from SNP vectors.

Architecture:

- Fully connected feed-forward network
- ReLU activations
- Cross-entropy optimization using Adam

---

# Key Results

- Identification accuracy remained highly robust up to approximately **50% SNP degradation**.
- Performance declined sharply at **70–90% degradation levels**.
- Balanced DNA mixtures produced the highest uncertainty and entropy.
- Dominant-contributor mixtures yielded stronger confidence scores.
- PCA visualization demonstrated clear separation between individuals and mixed genomic profiles.
- Deep learning models successfully learned latent genomic embeddings, though overfitting emerged under limited identity supervision.

---

# Figures

## Identification Accuracy Under DNA Degradation

![Identification Accuracy](figures/identification_accuracy_vs_degradation.png)

---

## Mixture Balance vs Entropy

![Mixture Entropy](figures/mixture_balance_vs_entropy.png)

---

## PCA Visualization of Mixed DNA Samples

![PCA Mixed Samples](figures/pca_mixed_dna_samples.png)

---

## Deep Genomic Embedding Space

![Deep Embedding Space](figures/deep_genomic_embedding_space.png)

---

## Mixture Similarity Scores

![Mixture Similarity](figures/mixture_similarity_scores.png)

---

## Mean Genotype Distribution Across Individuals

![Mean Genotype](figures/mean_genotype_per_individual.png)

---

## Deep Learning Training Curve

![Training Curve](figures/neural_network_training_curve.png)

---

## Posterior Identity Probabilities

![Posterior Identity](figures/Posterior%20probabilities%20of%20membership%20in%20mixture%20component%201.png)

---

## ROC Curve for Genomic Identification

![ROC Curve](figures/roccurve_genomic_identification.png)

---


# Technologies Used

- Python
- NumPy
- SciPy
- scikit-learn
- scikit-allel
- Matplotlib
- PyTorch
- Jupyter Notebook

---

# Project Structure

```text
genomic_identification/
│
├── figures/
├── notebooks/
├── results/
├── src/
├── README.md
└── requirements.txt
```

---

# Future Directions

- Bayesian probabilistic genomic inference
- Transformer-based genomic embeddings
- Contrastive learning for identity matching
- Population-aware forensic inference
- Ancient DNA degradation modeling
- GPU-scale training on full 1000 Genomes datasets

---

# Author

**Agata Gabara**

Computational Genomics / Bioinformatics / Machine Learning  
Vrije Universiteit Amsterdam
