# STAGATE_pyG
STAGATE software based on pyG (PyTorch Geometric) framework.

![](https://github.com/QIFEIDKN/STAGATE/blob/main/STAGATE_Overview.png)

## News
2022.03.05 STAGATE based on pyG (PyTorch Geometric) framework is availble at [STAGATE_pyG](https://github.com/QIFEIDKN/STAGATE_pyG).

Benefit from the optimization of the pyG package for training graph neural networks, it is more than 10x faster than STAGATE based on the tensorflow1 framework, and can use a batch training strategy to deal with large-scale data.

## Overview
STAGATE is designed for spatial clustering and denoising expressions of spatial resolved transcriptomics (ST) data.

STAGATE learns low-dimensional latent embeddings with both spatial information and gene expressions via a graph attention auto-encoder. The method adopts an attention mechanism in the middle layer of the encoder and decoder, which adaptively learns the edge weights of spatial neighbor networks, and further uses them to update the spot representation by collectively aggregating information from its neighbors. The latent embeddings and the reconstructed expression profiles can be used to downstream tasks such as spatial domain identification, visualization, spatial trajectory inference, data denoising and 3D expression domain extraction.

STAGATE based on tensorflow framework can be found at [here](https://github.com/QIFEIDKN/STAGATE).

## Getting started
See [Documentation and Tutorials](https://stagate.readthedocs.io/en/latest/index.html).

## Software dependencies
scanpy

pytorch

pyG

## Installation
cd STAGATE_pyG-main

python setup.py build

python setup.py install

## Citation
Dong, Kangning, and Shihua Zhang. “Deciphering spatial domains from spatially resolved transcriptomics with adaptive graph attention auto-encoder.” bioRxiv (2021). doi: https://doi.org/10.1101/2021.08.21.457240
