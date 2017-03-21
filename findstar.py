import sys
import csv
from collections import namedtuple
import heapq

h = []

try:

    capacity = int(sys.argv[1])

    
    reader = csv.reader(sys.stdin)
    Data = namedtuple("Data", next(reader))
    for data in map(Data._make, reader):
        if len(h)< capacity:
             heapq.heappush(h, (-float(data.dist),[float(data.x),float(data.y),float(data.z)]))
        elif float(data.dist)>h[0][0]:
             heapq.heappop(h)
             heapq.heappush(h, (-float(data.dist),[float(data.x),float(data.y),float(data.z)]))
    for i in range(len(h)):
        print(-h[i][0],h[i][1])


    
    
except ValueError:
    print("Please enter an integer")
