import pandas as pd
import numpy as np
from scipy.spatial import distance
from geopy.distance import geodesic
import os
from math import radians, degrees, sin, cos, asin, acos, sqrt

def edges2csv(graph_dir, edges_dir, metric='euclid'):
    """
    Arguements:
        graph_dir: The file path to the directory containing the .tsp files
        edges_dir: The file path to the directory containing the .edges files
        metric: Euclidean or Geodesic for distance between points.
    """
    
    graph_files = [i for i in os.listdir(graph_dir) if i.endswith('.tsp')]
    edge_files = [i for i in os.listdir(edges_dir) if i.endswith('.edges')]
    
    num_files = len(graph_files)
    
    assert(len(graph_files) == len(edge_files)) # Check to see same amount of files
    
    for i in range(num_files):
        df_edges = pd.read_csv(edges_dir + 'Graph{}.edges'.format(i), delimiter=' ', skiprows=[0], names=['Node1_ID', 'Node2_ID', 'DISTANCE_KM'])
        df_graph = pd.read_csv(graph_dir + '/Graph{}.tsp'.format(i), delimiter=' ', skiprows=[j for j in range(6)], names=['NODE_ID', 'LATITUDE', 'LONGITUDE'])
        
        df_edges = df_edges.join(df_graph, how='left', on='Node1_ID') \
        .rename(columns={'LONGITUDE': 'LONGITUDE_NODE_1', 
                         'LATITUDE': 'LATITUDE_NODE_1'})      \
        .drop('NODE_ID', axis=1)
        
        df_edges = df_edges.join(df_graph, how='left', on='Node2_ID') \
        .rename(columns={'LONGITUDE': 'LONGITUDE_NODE_2', 
                         'LATITUDE': 'LATITUDE_NODE_2'})      \
        .drop('NODE_ID', axis=1)
        
        df_edges['EDGE(Node1_ID, Node2_ID)'] = list(zip(df_edges['Node1_ID'], df_edges['Node2_ID']))
        df_edges = df_edges.drop(['Node1_ID', 'Node2_ID'], axis=1)
        
        df_edges['NODE1_COORDS'] = list(zip(df_edges['LATITUDE_NODE_1'], df_edges['LONGITUDE_NODE_1']))
        df_edges = df_edges.drop(['LONGITUDE_NODE_1', 'LATITUDE_NODE_1'], axis=1)
        
        df_edges['NODE2_COORDS'] = list(zip(df_edges['LATITUDE_NODE_2'], df_edges['LONGITUDE_NODE_2']))
        df_edges = df_edges.drop(['LONGITUDE_NODE_2', 'LATITUDE_NODE_2'], axis=1)
        
        df_edges['GEODESIC_DISTANCE_KM'] = pd.Series(list(zip(df_edges['NODE1_COORDS'], df_edges['NODE2_COORDS']))).apply(lambda x: geodesic(x[0], x[1]).kilometers) # Geodesic distance between coordinates
        df_edges['GEODESIC_ROUNDED_DISTANCE_KM'] = df_edges['GEODESIC_DISTANCE_KM'].apply(np.round) # Geodesic rounded distance between Coordinates
        
        df_edges['NODE1_COORDS'] = df_edges['NODE1_COORDS'].apply(lambda x: tuple(np.round(x, decimals=6)))
        df_edges['NODE2_COORDS'] = df_edges['NODE2_COORDS'].apply(lambda x: tuple(np.round(x, decimals=6)))
        
        df_edges.to_csv('./Graph{}.csv'.format(i), index=False, float_format='%.6f')
        
        print('Completed Graph{}.csv'.format(i))

