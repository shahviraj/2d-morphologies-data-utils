"""
Analysis functions
"""

import numpy as np
from PIL import Image
import os
import seaborn as sns

def get_p1_value(x):
    """
    Returns p1 value for the image.
    """
    return x.mean()

def radial_profile(image, center, img_size):
    x, y = np.indices(image.shape)
    rad = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    ind = np.argsort(rad.flat)
    rad_sorted = rad.flat[ind]
    image_sorted = image.flat[ind]
    rad_round = rad_sorted.astype(int)
    deltar = rad_round[1:] - rad_round[:-1]
    nonzero_deltar = np.where(deltar > 0.0)[0]
    nind = nonzero_deltar[1:] - nonzero_deltar[:-1]
    yvalues = np.cumsum(image_sorted, dtype = np.float64)
    yvalues = yvalues[nonzero_deltar[1:]] - yvalues[nonzero_deltar[:-1]]
    radial_var = yvalues/nind
    radial_dis = rad_round[nonzero_deltar]/(min(image.shape))
    return radial_var, radial_dis[:-1]

def get_p2_vector(img):
    """
    Returns a p2 vector.
    We calculate the p2 vector by taking the radial mean of 
    the autocorrelation of the input image.
    """
    radvars = []
    dimX = img.shape[0]
    dimY = img.shape[1]
    fftimage = np.fft.fft2(img)
    final_image = np.fft.ifft2(fftimage*np.conj(fftimage))
    finImg = np.abs(final_image)/(dimX*dimY)
    centrdImg = np.fft.fftshift(finImg)
    center = [int(dimX/2), int(dimY/2)]
    radvar, _ = radial_profile(centrdImg, center, (dimX, dimY))
    radvars.append(radvar)
    p2_vec = np.array(radvars)
    return p2_vec[0]

def get_dataset_p1_distribution(ds, bins=100):
    """
    Return the p1 distribution over the dataset or a segment of the same
    Params:
        ds: AIRADataset instance or AIRADataset iterator
        bins: # of bins for the histogram
    Returns:
        Histogram of distribution
    """
    p1_s = []
    for i in ds:
        p1_s.append(get_p1_value(i))
    ax = sns.distplot(p1_s)
    return ax

def get_segmented_ds(ds, p1_range):
    p1_s = np.asarray([get_p1_value(i) for i in ds])
    p1_max = p1_s.max()
    p1_min = p1_s.min()
    if p1_range[0] < p1_min  or p1_range[1] > p1_max:
        raise Exception('P1 values out range. Dataset has samples within p1_ranges: [{}, {}]'.format(p1_min, p1_max))
    indices = [i for i in range(len(p1_s)) if ((p1_s[i] >= p1_range[0]) and (p1_s[i]<=p1_range[1]))]
    ds_filtered = np.asarray([ds[i] for i in indices])
    return ds_filtered

    