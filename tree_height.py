#Python3

import os
import sys
import threading

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
    # get input type (k - keyboard, F - file)
    input_type = input("Input type (k - keyboard, F - file): ").strip().lower()
    
    # get input
    if input_type == 'k':
        # keyboard input
        n = int(input())
        parents = list(map(int, input().split()))
    elif input_type == 'f':
        # file input
        filename = input("Enter file name (without letter 'a'): ")
        if 'a' in filename:
            print("Invalid file name")
            return
        if not os.path.isfile(f"folder/{filename}"):
            print("File not found.")
            return
        with open(f"folder/{filename}", 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
        return
    
    # compute and output height
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()