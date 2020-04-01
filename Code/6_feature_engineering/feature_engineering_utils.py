import pandas as pd
import multiprocessing
import os


def edges_incident_to_edge(edge_series, edge):
    """
    This function will get the list of edges that are incident to the 2 nodes that create our target edge.

    :param edge_series: pd.Series object containing a list of edges
    :param edge: the target edge (tuple)
    :return: pd.Series object of edges incident to the target edge
    """

    assert isinstance(edge, tuple)
    assert isinstance(edge_series, pd.Series)

    node1 = edge[0]
    node2 = edge[1]

    edges_in_node1 = edge_series[edge_series.apply(lambda x: node1 in x)]
    edges_in_node2 = edge_series[edge_series.apply(lambda x: node2 in x)]

    edges_incident = edges_in_node1.append(edges_in_node2).reset_index(drop=True)
    edges_incident = edges_incident.drop_duplicates()

    return edges_incident


def local_edge_rank(df_TSP, edge, metric='DISTANCE_KM'):
    """
    This function will calculate the rank of the target edge

    :param df_TSP: A DataFrame containing all the data from the TSP (pd.DataFrame)
    :param edge: the target edge (tuple)
    :param metric: An optional argument that can alter how the ranking is computed (str)
    :return: The scaler rank of the target edge
    """

    assert isinstance(df_TSP, pd.DataFrame)
    assert isinstance(edge, tuple)
    assert isinstance(metric, str)
    assert metric in df_TSP.columns

    df_in_edges = edges_incident_to_edge(df_TSP['EDGE(Node1_ID, Node2_ID)'], edge).to_frame()
    df_in_edges = pd.merge(df_in_edges, df_TSP, on='EDGE(Node1_ID, Node2_ID)')
    df_in_edges = df_in_edges.sort_values(metric)
    df_in_edges['RANK'] = range(1, len(df_in_edges) + 1)

    assert len(df_in_edges[df_in_edges['EDGE(Node1_ID, Node2_ID)'] == edge]) == 1

    rank = int(df_in_edges[df_in_edges['EDGE(Node1_ID, Node2_ID)'] == edge]['RANK'])

    return rank

