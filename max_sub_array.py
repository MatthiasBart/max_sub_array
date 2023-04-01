"""
Find a contiguous subarray with the largest sum, within a given one-dimensional array a[l...r]
of numbers with three different algorithms: brute force, divide and conquer and scan line
"""

from array import array


def brute_force(a: array, l: int, r: int) -> int:
    """
    Calculate maximum subarray result with brute force method
    :param a: array of numbers
    :param l: left boundary index of array
    :param r: right boundary index of array
    :return: maximum sum of all contiguous sub-arrays
    """

    # Begin implementation
    max_sum = 0
    for left in range(l, r + 1):
        for right in range(left, r + 1):
            sum = 0
            for index in range(left, right + 1):
                sum = sum + a[index]
            max_sum = max(max_sum, sum)
    return max_sum
    # End implementation

def rmax(a: array, begin, end) -> int:
    sum = 0
    max_right = 0
    for i in range(begin, end + 1):
        sum = sum + a[i]
        max_right = max(max_right, sum)
    return max_right

def lmax(a: array, begin, end) -> int:
    sum = 0
    max_left = 0
    for i in range(end, begin -1, -1):
        sum = sum + a[i]
        max_left = max(max_left, sum)
    return max_left

def divide_and_conquer(a: array, l: int, r: int) -> int:
    """
    Calculate maximum subarray result with divide and conquer method
    :param a: array of numbers
    :param l: left boundary index of array
    :param r: right boundary index of array
    :return: maximum sum of all contiguous sub-arrays
    """

    # Begin implementation
    if r == l:
        if a[l] > 0: return a[l]
        return 0
    else:
        middle = int((r+l)/2)
        return max(divide_and_conquer(a, l, middle), divide_and_conquer(a, middle + 1, r), rmax(a, middle + 1, r) + lmax(a, l, middle))
    # End implementation


def scan_line(a: array, l: int, r: int) -> int:
    """
    Calculate maximum subarray result with scan line method
    :param a: array of numbers
    :param l: left boundary index of array
    :param r: right boundary index of array
    :return: maximum sum of all contiguous sub-arrays
    """

    # Begin implementation
    scanMax = 0
    bisMax = 0
    for i in range(l,r + 1):
        scanMax = max(0, scanMax + a[i])
        bisMax = max(scanMax, bisMax)
    return bisMax
    # End implementation

# Add your auxiliary methods here
# Begin implementation

# End implementation
