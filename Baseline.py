# Option:2 Longest Cubic Subsequence
from itertools import combinations

#check if a string consists of three identical blocks
def is_cubic(squence):
    n = len(squence)

    if n % 3 != 0:
        return False

    k = n // 3

    #Divide the string into three equal length blocks
    first = squence[:k]
    second = squence[k:2*k]
    third = squence[2*k:]

    return first == second == third

def lognest_sub_squares(sequence):
    n = len(sequence)

    #check candidate lengths from largest to smallest
    for length in range(n - n % 3, 0, -3):
        #generate all subsequences of their current length
        for i in combinations(range(n), length):
            solution = "".join(sequence[index] for index in i)
            #return when a valid cubic subsequence is found
            if is_cubic(solution):
                return solution

    # No valid cubic subsequence
    return ""


def main():
    #example input
    sequence = "atcgtatgcatgca"

    result = lognest_sub_squares(sequence)

    print("input:", sequence)
    print("output:", result)
    print("length:", len(result))

main() 