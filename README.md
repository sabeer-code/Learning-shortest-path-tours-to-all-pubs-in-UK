# Learning-shortest-path-tours-to-all-pubs-in-UK

The problem is to find a shortest tour covering each of the 49,687 pub crawls in UK (a large instance of the classic Travelling Salesman Problem). Travelling Salesman Problem (TSP) is an NP-hard problem and even for 50 cities, the world's fastest supercomputer has no hope of going through the full count of tours one by one to pick out the shortest. So, it may seem very daunting. However, the state-of-the-art heuristics have already solved this instance, to within 1 meter of accuracy (http://www.math.uwaterloo.ca/tsp/uk/index.html), in around 250 years of computer time.

The goal of this project is to explore if it is possible to learn the shortest tour in a supervised manner. In other words, a classification model is required to be learnt that can predict the edges in the shortest TSP tour based on the features of edges. It is hoped that the learning approach would compute close-to-optimal solution in significantly less computation time.

Watching material: https://www.youtube.com/watch?v=5VjphFYQKj8