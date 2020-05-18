import pandas as pd
import numpy as np
import os

#os.environ['PROJ_LIB'] = os.environ['CONDA_PREFIX'] + os.sep+ 'Library' + os.sep + 'share' # bug fix with anaconda and basemap (Windows)
os.environ['PROJ_LIB'] = os.environ['CONDA_PREFIX'] + os.sep+ 'share' + os.sep + 'proj' # bug fix with anaconda and basemap (Linux)
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def prune_ratio(predicted_tour, max_edges):
    """
    This function will return the number of edges that predicted by the model that were in the ground truth,
    divided by the total number of edges predicted by the model.
    
    Argument: 
    predicted_tour: The DataFrame containing the tour
    node_num: The number of nodes in the graph
    """
    
    edges_in_tour = predicted_tour.shape[0]

    return 1 - (edges_in_tour / max_edges)


def precision(predicted_tour):
    """
    This will calculate the precision of the model output.
    """
    if predicted_tour.shape[0] == 0:
        return 1
    else:
        return ground_truth_count(predicted_tour)/predicted_tour.shape[0]

    

def ground_truth_count(predicted_tour):
    """
    This function will return the number of the ground truth edges are in the predicted tour.
    """
    if predicted_tour.shape[0] == 0:
        return 0 # No ground truth edges predicted
    else:
        return predicted_tour['EDGE_IN_SOL'].astype(int).sum()
    
    
def threshold_tour(X, df_coords, model, threshold=0.5):
    """
    This function will create a tour using a threshold value.
    """
    assert hasattr(model, 'predict_proba')
    
    y = model.predict_proba(X)
    y = y[:, 1]
    y = np.where(y > threshold, 1, 0)
    
    return df_coords[y == 1]
