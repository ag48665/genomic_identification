import streamlit as st
import os

st.set_page_config(
    page_title="Genomic Identification",
    layout="wide"
)

st.title("Computational Methods for Human Identification")
st.subheader("Forensic Genomics + Deep Learning + Bayesian Inference")

st.markdown("""
This project investigates forensic-style genomic identification
from degraded and mixed DNA samples using machine learning,
probabilistic inference, and population-aware genomics.
""")

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Choose Section",
  [
    "Overview",
    "Population Structure",
    "Ancestry Inference",
    "Bayesian Inference",
    "Explainable Genomic AI",
    "Deep Genomic Embeddings"
]
)

FIG_DIR = "figures"

def show_figure(filename, caption=None):
    path = os.path.join(FIG_DIR, filename)

    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing file: {filename}")

if section == "Overview":

    st.header("Project Overview")

    st.markdown("""
    Computational genomics framework for:
    
    - degraded DNA analysis
    - mixed DNA inference
    - ancestry prediction
    - Bayesian uncertainty modeling
    - explainable genomic AI
    """)

if section == "Population Structure":

    st.header("Population Structure")

    show_figure("population_umap_structure.png")

    show_figure("population_aware_pca.png")

if section == "Ancestry Inference":

    st.header("Ancestry Inference")

    show_figure("Ancestry Inference Confusion Matrix.png")

    show_figure("ancestry_multiclass_roc.png")

if section == "Bayesian Inference":

    st.header("Bayesian Identity Inference")

    show_figure("bayesian_posterior_identity.png")

    show_figure("bayesian_identity_uncertainty.png")

if section == "Explainable Genomic AI":

    st.header("Explainable Genomic AI")

    show_figure("explainable_snp_importance.png")

    show_figure("snp_feature_importance.png")

if section == "Deep Genomic Embeddings":

    st.header("Deep Genomic Embeddings")

    st.markdown("""
    Neural autoencoders were trained on SNP matrices
    to learn compressed latent genomic representations.

    The learned embeddings capture hidden genomic structure
    across individuals in a reduced latent space.
    """)

    show_figure("Learned Latent Genomic Representation.png")

    show_figure("Autoencoder Training Loss.png")

