import sys

import random

n = int(sys.stdin.readline())

def generate_routes():
    for c1 in range(0, n):
        for c2 in range(c1 + 1, n):
            are_connected = random.random() < 0.6
            construction_cost = random.randint(1, 20)
            yield (c1, c2, are_connected, construction_cost)

print(n)

for (c1, c2, are_connected, construction_cost) in generate_routes():
    print(str(c1) + " " +
          str(c2) + " " +
          ("1 " if are_connected else "0 ") +
          str(construction_cost))
