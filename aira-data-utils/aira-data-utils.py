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

_DATA_URL_TINY = 'https://drive.google.com/file/d/1VKcANpq428u0_cjssQdTlBuCgmzN4Npc/view?usp=sharing'
_DATA_URL_HUGE = 'https://drive.google.com/file/d/1VKcANpq428u0_cjssQdTlBuCgmzN4Npc/view?usp=sharing'
_DKEY = 'morphology'
_IMG_SIZE = 101

class AIRADataset():
    """
    Class to handle the AIRA dataset. 
    Supports downloading and visualizing the dataset.
    """

    def __init__(self, dataset_path, dataset_type='tiny', download=True):
        self.dtype = dataset
        self.dpath = dataset_path
        if self.dtype == 'tiny':
            self.data_url = _DATA_URL_TINY
        else:
            self.data_url = _DATA_URL_HUGE
        if download:
            self.download_dataset(self.dpath)
        else:
            try:
                self.data = h5py.File(self.dpath, mode='r')[_DKEY]
            except:
                raise Exception('Unable to open file. Download manually from {}'.format(self.data_url))
        self.len = len(self.data)
        
    def download_dataset(self, datapath):
        try:
            r = requests.get(self.data_url)
            open(self.dpath,'wb').write(r.content)
        except:
            raise Exception('Unable to download file from {}'.format(self.data_url))

    def __getitem__(self, index):
        return self.data[index, ...].reshape((_IMG_SIZE, _IMG_SIZE))
    
    def __len__(self):
        return self.len

    def get_dataset(self):
        return self.data
    
    def show_random_images(self):
        tile_img = self.generate_thumbnails(num_images=16)
        plt.imshow(tile_img)
        plt.show()

    def generate_thumbnails(self, num_images=16):
        random_indices = list(np.random.randint(0, self.len, size=num_images))
        r_imgs = np.array([np.pad(self.data[idx].reshape((_IMG_SIZE, _IMG_SIZE)), ((5,5),(5,5)), mode='constant', constant_values=((0,0),(0,0))) for idx in random_indices])
        tile_img = np.hstack(np.hstack(r_imgs))
        return tile_img    

class AIRAAnalysis():
    """
    Support basic analysis of dataset
    """

    def __init__(self, dataset):
        self.dataset = dataset
    
    def p1_histogram(self, idx_range):
        pass
    
    def p2_curve(self, idx):
        pass
    
        
if __name__ == '__main__':

    dpath = ''