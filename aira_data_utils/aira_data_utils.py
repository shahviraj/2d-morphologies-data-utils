#!/usr/env/bin python3
"""
Data utilities for AIRA Material Science Dataset
"""

import os
import numpy as np
import argparse as ap
import requests
import h5py
from matplotlib import pyplot as plt
from PIL import Image

_DATA_URL_HUGE = 'https://zenodo.org/record/2580293/files/2D_binary_morphologies.h5?download=1'
_DATA_URL_TINY = 'https://zenodo.org/record/2580293/files/2D_binary_morphologies.h5?download=1'

_DKEY = 'morphology'
_IMG_SIZE = 101

class AIRADataset():
    """
    Class to handle the AIRA dataset. 
    Supports downloading and visualizing the dataset.
    """

    def __init__(self, dataset_path, dataset_type='tiny', download=False, img_size=101):
        """
        Params:
            dataset_path: Path of the stored dataset if download=='False'.
                          Path to store the downloaded dataset at if download='True'.
            dataset_type: 'tiny' for the 2d-morph-tiny dataset.
                          'huge' for the 2d-morph-huge dataset.
            download: Flag ascertaiing wheter to download dataset or not. Requires dataset path.
            img_size: integer defining the output size of the samples. Default: 101
        """
        self.dtype = dataset_type
        self.dpath = dataset_path
        if self.dtype == 'tiny':
            self.data_url = _DATA_URL_TINY
        else:
            self.data_url = _DATA_URL_HUGE
        if download:
            self.download_dataset(self.dpath)
        self.f = h5py.File(self.dpath, mode='r')
        self.data = self.f[_DKEY]
        if not self.data:
            raise Exception('Unable to open file. Download manually from {}'.format(self.data_url))
        self.len = len(self.data)
        self.img_size = img_size
        
    def download_dataset(self, datapath):
        try:
            r = requests.get(self.data_url)
            open(self.dpath,'wb').write(r.content)
        except:
            raise Exception('Unable to download file from {}'.format(self.data_url))

    def __getitem__(self, key):
        if isinstance(key, slice):
           sliced_data = self.data[key,...].reshape((-1, _IMG_SIZE, _IMG_SIZE))
           # print(sliced_data.shape)
           orig_data = np.asarray([np.array(Image.fromarray(i).resize((self.img_size, self.img_size), resample=Image.LANCZOS)) for i in sliced_data])
        elif isinstance(key, int):
            if key < 0:
                key += self.len
            if key >= self.len or key < 0:
                raise IndexError('Index {} out of range'.format(key))
            orig_data = np.array(Image.fromarray(self.data[key, ...].reshape((_IMG_SIZE, _IMG_SIZE))).resize((self.img_size, self.img_size), resample=Image.LANCZOS))
        else:
            raise TypeError('Invalid Argument Type')
        return orig_data

    def __len__(self):
        return self.len

    def __del__(self):
        # Cleanup
        self.f.close()

    def get_dataset(self):
        return self.data
    
    def show_random_images(self):
        tile_img = self.generate_thumbnails(num_images=16)
        plt.imshow(tile_img, cmap='gray')
        plt.show()

    def generate_thumbnails(self, num_images=16):
        random_indices = list(np.random.randint(0, self.len, size=num_images))
        r_imgs = np.array([np.pad(np.array(Image.fromarray(self.data[idx].reshape((_IMG_SIZE, _IMG_SIZE))).resize((self.img_size, self.img_size))),
                            ((5,5),(5,5)), mode='constant', constant_values=((1,1),(1,1))) for idx in random_indices])
        r_imgs = r_imgs.reshape((4,4,self.img_size+10, self.img_size+10))
        tile_img = np.hstack(np.hstack(r_imgs))
        return tile_img    