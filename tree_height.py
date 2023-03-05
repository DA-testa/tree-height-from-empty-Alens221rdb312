# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    children = {}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in children:
                children[parent] = []
            children[parent].append(i)
    # Your code here
    def compute_subtree_height(node):
        if node not in children:
            return 1
        subtree_heights = [compute_subtree_height(child) for child in children[node]]
        return max(subtree_heights) + 1
    
    return compute_subtree_height(root)

def main():
    # implement input form keyboard and from files
    input_type = input("Input type (k - keyboard, F - file): ").strip().lower()
    
    
    if input_type == 'k':

        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parent seperated by space: ").split()))
    elif input_type == 'f':
        while True:
            try:
                filename = input("Enter file name (without letter 'a'): ")    
                if 'a' in filename:
                    raise ValueError("File name cannot contain letter 'a'.")
    
                with open(f"folder/{filename}", 'r') as f:
                    n = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
                break
            except FileNotFoundError:
                print("File not found.")
            except ValueError as e:
                print(e)
        else:
            print("Invalid input type.")
            return

        print("Tree height:",compute_height(n, parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))