#Python3

import sys
import threading
import numpy
import os


def compute_height(n, parents):
    # Write this function
    max_height = 0
    heights = [0] * n
    for vertex in range(n):
        if heights[vertex] != 0:
            continue
        height = 0
        i = vertex
        while i != -1:
            if heights[i] != 0:
                height += heights[i]
                break
            height += 1
            i = parents[i]
        max_height = max(max_height, height)
        i = vertex
        while i != -1:
            if heights[i] != 0:
                break
            heights[i] = height
            height -= 1
            i = parents[i]
    return max_height


def main():
    input_type = input("Input type (k - keyboard, F - file): ").strip().lower()
    while input_type not in ['k', 'f']:
        print("Invalid input type. Please enter 'k' or 'F'.")
        input_type = input("Input type (k - keyboard, F - file): ").strip().lower()
    if input_type == 'k':
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents of nodes separated by spaces: ").split()))
    else:
        filename = input("Enter file name (without letter 'a'): ")
        while 'a' in filename:
            print("File name cannot contain the letter 'a'.")
            filename = input("Enter file name (without letter 'a'): ")
        if not os.path.exists('inputs/' + filename):
            print("File not found.")
            return
        with open('inputs/' + filename) as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()