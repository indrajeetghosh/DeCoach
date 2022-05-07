import pandas as pd
import numpy as np
from numpy import array, mean, std, dstack,argmax


def normalize(X_Raw_Data):
    result = df4.copy()
    for feature_name in df4.columns:
        max_value = df4[feature_name].max()
        min_value = df4[feature_name].min()
        result[feature_name] = (df4[feature_name] - min_value) / (max_value - min_value)
    return result