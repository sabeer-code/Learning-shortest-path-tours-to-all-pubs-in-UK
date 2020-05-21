# Learning-shortest-path-tours-to-all-pubs-in-UK

The problem is to find a shortest tour covering each of the 49,687 pub crawls in UK (a large instance of the classic Travelling Salesman Problem). Travelling Salesman Problem (TSP) is an NP-hard problem and even for 50 cities, the world's fastest supercomputer has no hope of going through the full count of tours one by one to pick out the shortest. So, it may seem very daunting. However, the state-of-the-art heuristics have already solved this instance, to within 1 meter of accuracy (http://www.math.uwaterloo.ca/tsp/uk/index.html), in around 250 years of computer time.

The goal of this project is to explore if it is possible to learn the shortest tour in a supervised manner. In other words, a classification model is required to be learnt that can predict the edges in the shortest TSP tour based on the features of edges. It is hoped that the learning approach would compute close-to-optimal solution in significantly less computation time.

Watching material: https://www.youtube.com/watch?v=5VjphFYQKj8

---

## Setup

### Anaconda Environment
Import the environment using the `requirements.yaml` file using the Anaconda Navigator GUI or you can enter these commands in your shell:


```
$ conda env create -f requirements.yaml
```

### Concorde TSP Solver
Instructions on how to download and build the concorde for you system can be found [here](http://www.math.uwaterloo.ca/tsp/concorde/downloads/downloads.htm).


## How to run

1) Activate the environment using:
```
$ conda activate TSP_Problem
```

2) Scraping the pub data from the [Pubs Galore](www.pubsgalore.co.uk) website. Firstly navigate to the directory `Code/1_pubs_crawler` and execute the following command in your shell.
```
(TSP_Problem) $ scrapy crawl pubs
```

3) The other directories are numbered and the rest of the code should be ran in that order using jupyter lab or jupyter notebook.
```
(TSP_Problem) $ jupyter notebook
```
or
```
(TSP_Problem) $ jupyter lab
```

## Contributors
- Deepak Ajwani (deepak.ajwani@ucd.ie)
- Sabeer Bakir (sabeer.bakir@ucdconnect.ie)