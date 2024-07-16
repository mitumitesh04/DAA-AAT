
import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
from collections import defaultdict

def maximumPeople(towns, cloud_start, cloud_end):
    towns.sort()
    cloud_start.sort()
    cloud_end.sort()

    cloud_start_index = 0
    cloud_end_index = 0
    active_clouds = set()

    population_under_clouds = defaultdict(int)
    population_free_of_clouds = 0

    for town_index in range(len(towns)):
        town_location = towns[town_index][0]

        while cloud_start_index < len(cloud_start) and cloud_start[cloud_start_index][0] <= town_location:
            active_clouds.add(cloud_start[cloud_start_index][1])
            cloud_start_index += 1

        while cloud_end_index < len(cloud_end) and cloud_end[cloud_end_index][0] < town_location:
            active_clouds.remove(cloud_end[cloud_end_index][1])
            cloud_end_index += 1

        if len(active_clouds) == 1:
            towns[town_index][2] = list(active_clouds)[0]
            population_under_clouds[list(active_clouds)[0]] += towns[town_index][1]
        elif len(active_clouds) == 0:
            population_free_of_clouds += towns[town_index][1]

    return max(population_under_clouds.values(), default=0) + population_free_of_clouds

def main():
    n = int(input().strip())
    populations = list(map(int, input().strip().split()))
    locations = list(map(int, input().strip().split()))
    towns = [[locations[i], populations[i], -1] for i in range(n)]

    m = int(input().strip())
    cloud_centers = list(map(int, input().strip().split()))
    cloud_ranges = list(map(int, input().strip().split()))

    cloud_start = [[cloud_centers[i] - cloud_ranges[i], i] for i in range(m)]
    cloud_end = [[cloud_centers[i] + cloud_ranges[i], i] for i in range(m)]

    result = maximumPeople(towns, cloud_start, cloud_end)
    print(result)

if __name__ == "__main__":
    main()