# python3

# 221RDB312 Alens Ilgavižs 4.grupa

import sys
import threading
#import numpy

def compute_height(n, parents):
    # Write this function
    tree = {}
    for i in range(n):
        tree[i] = []
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    #max_height = 0

    # Your code here
    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max(height(child) for child in tree[node])
    return height(root)


def main():

    # implement input form keyboard and from files
    text = input("Enter 'I' for input or 'F' for file")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        # account for github input inprecision
    elif "F" in text:
        path = './test/'
        file_name = input("Enter file name: ")
        folder = path + file_name
    # let user input file name to use, don't allow file names with letter a
        if 'a' in file_name:
            print("File is not allowed to contain letter 'a'")
            return
        try:
            with open(folder, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("Error: File not found")
            return
        except ValueError:
            print("Error: Invalid input format")
            return
    else:
        print("Enter 'I' or 'F':")
        return 
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
       
    # call the function and output it's result
    print(compute_height(n, parents))
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))