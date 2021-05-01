import copy
import random


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def full_permutations_recursive(array, i):
    if i == len(array):
        print(array)
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            full_permutations_recursive(array, i + 1)
            swap(array, i, j)


array = []
for i in range(1, 4):
    array.append(i)

full_permutations_recursive(array, 0)
