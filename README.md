# Simplified-GPS

### Problem Statement
It’s September, which means you have only 6 months to make your Spring Break vacation plans to a dream destination! We’ve prepared a dataset of major highway segments of the United States (and parts of southern Canada and northern Mexico), including highway names, distances, and speed limits; you can visualize this as a graph with nodes as towns and highway segments as edges. We’ve also prepared a dataset of cities and towns with corresponding latitude-longitude positions. These files should be in your GitHub repo from when you cloned in step 0. Your job is to implement algorithms that find good driving directions between pairs of cities given by the user. Your program should be run on the commandline like this:

python route.py [start-city] [end-city] [routing-option] [routing-algorithm]

where:
+ start-city and end-city are the cities we need a route between.
+ routing-option is one of:
  – segments finds a route with the fewest number of “turns” (i.e. edges of the graph)
  – distance finds a route with the shortest total distance
  – time finds the fastest route, for a car that always travels at the speed limit
  – scenic finds the route having the least possible distance spent on highways (which we define as roads with speed limits 55 mph or greater)
+ routing-algorithm is one of:
  – bfs uses breadth-first search
  – dfs uses depth-first search
  – ids uses iterative deepening search
  – astar uses A* search, with a suitable heuristic function

The output of your program should be a nicely-formatted, human-readable list of directions, including
travel times, distances, intermediate cities, and highway names, similar to what Google Maps or another
site might produce. In addition, the last line of output should have the following machine-readable
output about the route your code found:

[total-distance-in-miles] [total-time-in-hours] [start-city] [city-1] [city-2] ... [end-city]

Please be careful to follow these interface requirements so that we can test your code properly. For
instance, the last line of output might be:

51 1.0795 Bloomington,_Indiana Martinsville,_Indiana Jct_I-465_&_IN_37_S,_Indiana Indianapolis,_Indiana

Like any real-world dataset, our road network has mistakes and inconsistencies; in the example above, for example, the third city visited is a highway intersection instead of the name of a town. Some of these “towns” will not have latitude-longitude coordinates in the cities dataset; you should design your code to still work well in the face of these problems.

In the comment section at the top of your code file, please include a brief analysis of the results of your program, answering the questions: 
1. Which search algorithm seems to work best for each routing options? 
2. Which algorithm is fastest in terms of the amount of computation time required by your program, and by how much, according to your experiments? (To measure time accurately, you may want to temporarily include a loop in your program that runs the routing a few hundred or thousand times.)
3. Which algorithm requires the least memory, and by how much, according to your experiments?
4. Which heuristic function did you use, how good is it, and how might you make it better?
5. Supposing you start in Bloomington, which city should you travel to if you want to take the longest possible drive (in miles) that is still the shortest path to that city? (In other words, which city is furthest from Bloomington?)
