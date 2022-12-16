# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product

# load image data
df_image=pd.read_csv('image.csv')
df_image


# +
# make function to map between cartesian coordinaties and array indexes
def cartesian_to_array(x, y, shape):
    m, n=shape[:2]
    i=(n-1)//2-y
    j=(n-1)//2+x
    
    if i<0 or i>=m or j<0 or j>=n:
        raise ValueError('Coordinates not within given dimensions')
    return i, j
def array_to_cartesian(i, j, shape):
    m, n=shape[:2]
    if i<0 or i>=m or j<0 or j>=n:
        raise ValueError('Coordinates not within given dimensions')
    y=(n-1)//2-i
    x=j-(n-1)//2
    return x, y

point=(1, 8)
shape=(9, 9, 3)
assert cartesian_to_array(*array_to_cartesian(*point, shape), shape)==point


# +
# make function to map an image between array and record formats
def image_to_dict(image):
    image=np.atleast_3d(image)
    kv_image={}
    for i, j in product(range(len(image)), repeat=2):
        kv_image[array_to_cartesian(i, j, image.shape)]=tuple(image[i, j])
    return kv_image

def image_to_df(image):
    return pd.DataFrame([(x, y, r, g, b) for (x, y), (r, g, b) in image_to_dict(image).items()],
                       columns=['x', 'y', 'r', 'g', 'b'])

def df_to_image(df):
    side=int(len(df)**0.5) # assumes a square image
    return df.set_index(['x', 'y']).to_numpy().reshape(side, side, -1)


# +
image=df_to_image(df_image)
assert image_to_df(image).equals(df_image) # ensure transforms are inverses

radius=128
fig, ax=plt.subplots(figsize=(10, 10))
ax.matshow(image, extent=(-radius, radius+1, -radius, radius+1))
ax.grid(None);
# -
# #### These codes are from Kaggle competition's Santa 2022, the most voted code by Ryan Holbrook-Getting Started with Santa 2022
