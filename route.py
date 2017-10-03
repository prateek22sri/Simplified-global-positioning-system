#!/usr/bin/env python

import sys
from copy import deepcopy
from math import log, radians, sin, cos, asin, sqrt


class routingAlgorithm:
    """
    There are four routing algorithm to solve the routing problem:
    * bfs - ignores weights in the graph
    * uniform - bfs + considering the edge weights
    * dfs - ifnores weights in the graph
    * astar - has heuristic
    """

    def __init__(self):
        """
        Initializes all the data structures which belong to this class
        """
        self.startCity = ""
        self.endCity = ""
        self.algo = ""
        self.costFunct = ""
        self.city_gps = {}
        self.road_segments = {}
        self.visited = []

    def calculatePriority(self, s, pp, prevCity):
        """
        Calculates the total Priority needed for the priority queue
        returns a variable called tmp
        tmp = heuristic + cost
        :param s:
        :param pp:
        :param prevCity:
        :return: tmp
        """
        hx = 0
        cx = 0
        if self.algo == 'bfs' or self.algo == 'dfs':
            tmp = []
            for succ in s:
                # print(succ)
                tmp.append([succ, pp + 1])
            return tmp

        elif self.costFunct == 'segments':  # fewest edges
            tmp = []
            for succ in s:
                cx = 1
                if self.algo == 'astar':
                    hx = self.calculateHeuristic(succ[len(succ) - 1])
                tmp.append([succ, hx + cx + pp])
            return tmp
        elif self.costFunct == 'distance':  # shortest total distance
            tmp = []
            for succ in s:
                if prevCity in self.road_segments:
                    if succ[len(succ) - 1] in self.road_segments[prevCity]:
                        cx = int(self.road_segments[prevCity][succ[len(succ) - 1]][0])
                        if self.algo == 'astar':
                            hx = self.calculateHeuristic(succ[len(succ) - 1])
                        tmp.append([succ, hx + cx + pp])
            return tmp
        elif self.costFunct == 'time':  # time
            tmp = []
            for succ in s:
                if prevCity in self.road_segments:
                    if succ[len(succ) - 1] in self.road_segments[prevCity]:
                        cx = log(int(self.road_segments[prevCity][succ[len(succ) - 1]][1]))
                        if self.algo == 'astar':
                            hx = self.calculateHeuristic(succ[len(succ) - 1])
                        tmp.append([succ, cx + hx + pp])
            return tmp

    def uniformSuccessorFunction(self, s):
        """
        This is the successor function for all the algorithms in this code
        Combines the successor cities with their respective priority

        :param s:
        :return:
        """

        prevCity = s[0][len(s[0]) - 1]
        prevPriority = s[1]
        succList = []
        if prevCity in self.road_segments:
            for c in self.road_segments[prevCity]:
                if c not in self.visited:
                    succ = deepcopy(s[0])
                    succ.append(c)
                    succList.append(succ)

            newSuccList = self.calculatePriority(succList, prevPriority, prevCity)
            return newSuccList
        else:
            return None

    def bfs(self):
        """
        Implements Breadth First Search ignoring the distances or speed limits of the respective city/highways
        :return:
        """
        priority = int(0)
        fringe = []
        if self.startCity == self.endCity:
            return self.startCity
        fringe.append([[self.startCity], priority])
        while True:
            if not fringe:
                return "Failure"
            s = fringe.pop(0)
            if s[0][len(s[0]) - 1] == self.endCity:
                return s
            if s[0][len(s[0]) - 1] not in self.visited:
                self.visited.append(s[0][len(s[0]) - 1])
            else:
                continue
            successors = self.uniformSuccessorFunction(s)
            if successors:
                for successor in successors:
                    fringe.append(successor)

    def dfs(self):
        """
        Implements Depth First Search ignoring the distances or speed limits of the respective city/highways

        :return:
        """

        priority = int(0)
        fringe = []
        if self.startCity == self.endCity:
            return self.startCity
        fringe.append([[self.startCity], priority])
        while True:
            if not fringe:
                return "Failure"
            s = fringe.pop()

            if s[0][len(s[0]) - 1] == self.endCity:
                return s

            if s[0][len(s[0]) - 1] not in self.visited:
                self.visited.append(s[0][len(s[0]) - 1])
            else:
                continue
            successors = self.uniformSuccessorFunction(s)
            if successors:
                for successor in successors:
                    fringe.append(successor)

    def uniform(self):
        """
        Implements Breadth First Search considering all the distances or speed limits of the respective city/highways

        :return:
        """

        priority = int(0)
        fringe = []
        if self.startCity == self.endCity:
            return self.startCity
        fringe.append([[self.startCity], priority])
        while True:
            if not fringe:
                return "Failure"
            min = int(999999)
            for x in range(0, len(fringe)):
                if min > fringe[x][1]:
                    min = x
            s = fringe.pop(min)

            if s[0][len(s[0]) - 1] == self.endCity:
                return s

            if s[0][len(s[0]) - 1] not in self.visited:
                self.visited.append(s[0][len(s[0]) - 1])
            else:
                continue
            successors = self.uniformSuccessorFunction(s)
            if successors:
                for successor in successors:
                    fringe.append(successor)

    def aStar(self):
        """
        Implements A-Star Search considering the distances or speed limits of the respective city/highways

        :return:
        """
        priority = int(0)
        fringe = []
        if self.startCity == self.endCity:
            return self.startCity
        fringe.append([[self.startCity], priority])
        while True:
            if not fringe:
                return "Failure"
            min = int(999999)
            for x in range(0, len(fringe)):
                if min > fringe[x][1]:
                    min = x
            s = fringe.pop(min)

            if s[0][len(s[0]) - 1] == self.endCity:
                return s

            if s[0][len(s[0]) - 1] not in self.visited:
                self.visited.append(s[0][len(s[0]) - 1])
            else:
                continue
            successors = self.uniformSuccessorFunction(s)
            if successors:
                for successor in successors:
                    fringe.append(successor)

    def cityGPSReader(self):
        """
        This function reads the file city-gps.txt to populate the data structure city_gps which belongs to Class routingAlgorithm

        :return:
        """
        with open('city-gps.txt', 'r') as f:
            for line in f:
                tmp = line.strip('\n').split(' ')
                self.city_gps[tmp[0]] = [tmp[1], tmp[2]]

    def roadSegmentsReader(self):
        """
        This function reads the file road-segments.txt to populate the data structure road_segments which belongs to Class routingAlgorithm

        :return:
        """
        with open('road-segments.txt', 'r') as f:
            for line in f:
                tmp = line.strip('\n').split(' ')
                if len(tmp) == 5:
                    if tmp[0] not in self.road_segments:
                        self.road_segments[tmp[0]] = {tmp[1]: [tmp[2], tmp[3], tmp[4]]}
                    else:
                        self.road_segments[tmp[0]][tmp[1]] = [tmp[2], tmp[3], tmp[4]]
                else:
                    if tmp[0] not in self.road_segments:
                        self.road_segments[tmp[0]] = {tmp[1]: [tmp[2], 55, tmp[3]]}
                    else:
                        self.road_segments[tmp[0]][tmp[1]] = [tmp[2], 55, tmp[3]]
                if len(tmp) == 5:
                    if tmp[1] not in self.road_segments:
                        self.road_segments[tmp[1]] = {tmp[0]: [tmp[2], tmp[3], tmp[4]]}
                    else:
                        self.road_segments[tmp[1]][tmp[0]] = [tmp[2], tmp[3], tmp[4]]
                else:
                    if tmp[1] not in self.road_segments:
                        self.road_segments[tmp[1]] = {tmp[0]: [tmp[2], 55, tmp[3]]}
                    else:
                        self.road_segments[tmp[1]][tmp[0]] = [tmp[2], 55, tmp[3]]

    def calculateHeuristic(self, source):
        """
        This function calculates the heuristics of the code which is Great Circle Distance based off of the source's location from the Goal State
        Formula obtained from Wikipedia for Great Circle Distance - Original source Admirality Manual of Navigation, Volume 1
        link - https://en.wikipedia.org/wiki/Great-circle_distance

        :param source:
        :return:
        """
        if source not in self.city_gps:
            return 0
        latSource, longSource, latDest, longDest = map(radians,
                                                       [float(self.city_gps[source][0]),
                                                        float(self.city_gps[source][1]),
                                                        float(self.city_gps[self.endCity][0]),
                                                        float(self.city_gps[self.endCity][1])])
        latDiff = latSource - latDest
        longDiff = longSource - longDest
        hsine = sin(latDiff / 2) ** 2 + cos(latSource) * cos(latDest) * sin(longDiff / 2) ** 2
        return 6371 * 2 * asin(sqrt(hsine))

    def printResult(self, output):
        """
        This function prints the output of the format desired by the assignment

        :param output:
        :return: None
        """
        distance = 0
        time = 0
        for x in range(0, len(output[0]) - 2):
            distance += float(self.road_segments[output[0][x]][output[0][x + 1]][0])
            time += float(self.road_segments[output[0][x]][output[0][x + 1]][0]) / float(
                self.road_segments[output[0][x]][output[0][x + 1]][1])

        path = " ".join(output[0])

        print("Total estimated time in the route is ", time)
        print("Total estimated distance in the route is ", distance)
        print("Path is ", path)
        print("Machine Readable output:")
        print(time, distance, path)


def main():
    """
    Input : ./route.py [start-city] [end-city] [routing-algorithm] [cost-function]

    Cost function could be one of the following:
    * segments - least edges
    * distance - shortest total distance
    * time - fastest route i.e. routes with the highest speed limit

    Routing algorithm could be one of the following:
    * bfs
    * dfs
    * uniform
    * astar

    Machine readable output of the function would be of the following type:
    [total-distance-in-miles] [total-time-in-hours] [start-city] [city-1] [city-2] ... [end-city]
    """
    a = routingAlgorithm()
    if len(sys.argv) != 5:
        print("Usage : ./route.py [start-city] [end-city] [routing-algorithm] [cost-function]")
        exit(1)
    a.startCity, a.endCity, a.algo, a.costFunct = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    a.cityGPSReader()
    a.roadSegmentsReader()
    if a.algo == 'bfs':
        output = a.bfs()
    elif a.algo == 'dfs':
        output = a.dfs()
    elif a.algo == 'uniform':
        output = a.uniform()
    elif a.algo == 'astar':
        output = a.aStar()
    else:
        output = "Error: No output to print"
        exit(1)
    a.printResult(output)


if __name__ == '__main__':
    main()
