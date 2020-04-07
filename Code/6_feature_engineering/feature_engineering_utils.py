import pandas as pd


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


def edges_incident_to_node(df_TSP, node, metric='DISTANCE_KM'):
    """
    This function will get the list of edges that are incident to the 2 nodes that create our target edge.

    :param df_TSP: A DataFrame containing all the data from the TSP (pd.DataFrame)
    :param node: the target node (int)
    :param metric: a metric to use to sort edges
    :return: pd.DataFrame object of sorted edges incident to the target node and its weights
    """

    edge_series = df_TSP['EDGE(Node1_ID, Node2_ID)']

    assert isinstance(node, int)
    assert isinstance(edge_series, pd.Series)

    incident_edges = edge_series[edge_series.apply(lambda x: node in x)]
    df_out = df_TSP.merge(incident_edges)
    df_out = df_out[['EDGE(Node1_ID, Node2_ID)', 'DISTANCE_KM']]
    df_out = df_out.sort_values(metric)
    df_out = df_out.reset_index(drop=True)

    return df_out


def local_edge_rank_incident_to_node(df_nodes, node, edge):
    """
    This function calculates a rank value equal to the number of edges that have a
    higher distance metric.

    :param df_nodes: A pd.DataFrame object that contains a list of nodes and it's edges
    :param node: Target node (int)
    :param edge: Target edge (tuple)
    :return: Rank value (int)
    """

    assert isinstance(df_nodes, pd.DataFrame)
    assert isinstance(node, int)
    assert isinstance(edge, tuple)

    df_incident_edges = df_nodes.iloc[node]['Incident Edges']
    rank = df_incident_edges[df_incident_edges['EDGE(Node1_ID, Node2_ID)'] == edge].index[0]

    return rank


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

