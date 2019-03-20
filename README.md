
# Binary 2D morphologies of polymer phase separation

This repository contains supporting utilities for the 2D binary microstructure dataset. 
The dataset can be either automatically or manually downloaded.

[Download link](https://zenodo.org/record/2580293#.XHiGLi1KjmE)

The utilites support the following operations

1. Automatically downloading the dataset.
2. Iterating over the dataset to get images.
3. Show random thumbnails from the dataset.  

## Description

The dataset contains binary microstructure morphologies representing phase separation in polymer systems.

The dataset was generated through the simulation of a time evolving Cahn -Hilliard equation, describing phase separation in binary polymer blends. Several realizations of the equation were done through
different values of volume fractions and binary interaction parameters. Morphologies were outputted at constant time intervals.

File Format: The dataset is a HDF5 file containing a single dataset named 'morphology'. 

Dataset Size:  34672 images of 101x101 size.(Images stored as flattened row vectors of float values between 0.0 and 1.0)

## Usage:

Kindly refer to our [documentation](http://dice.ece.iastate.edu/img/ch_toolbox.pdf) for detailed API and utilities description. 

## Cite:

bibtex:
@misc{pokuri_balaji_sesha_sarath_2019_2580293,
  author       = {Pokuri, Balaji Sesha Sarath and
                  Shah, Viraj and
                  Joshi, Ameya and
                  Hegde, Chinmay and
                  Sarkar, Soumik and
                  Ganapathysubramanian, Baskar},
  title        = {{Binary 2D morphologies of polymer phase separation}},
  month        = feb,
  year         = 2019,
  doi          = {10.5281/zenodo.2580293},
  url          = {https://doi.org/10.5281/zenodo.2580293}
}
