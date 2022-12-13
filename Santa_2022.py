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
# -


