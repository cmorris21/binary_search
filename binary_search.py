#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    
    left = 0
    right = length(xs)-1
    
    def search(left, right):
        mid = (left + right)//2
        if 0 == xs[mid]:
            return xs[mid+1]
        if 0 > xs[mid]:
                    if 0 < xs[mid]:
            return search(left, mid-1)
        if 0 > xs[mid]:
            return search(mid+1, right)

    if len(xs) == 0:
        return None
    if xs[0] > 0:
        return 0
    else:
        return search(left, right)
          
        
def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    left = 0
    right = len(xs) - 1
   
    def search1(left,right):
        mid = (left + right)//2
        if xs[mid] == x:
            if mid == 0 or xs[mid-1] > x:
                return mid
            else:
                return search1(left, mid-1)
       
        if left == right:
            return None
        if x > xs[mid]:
            return search1(left, mid -1)
        if x < xs[mid]:
            return search1(mid + 1, right)

    def search2(left, right):
        mid = (left+ right)//2
        if xs[mid] == x:
            if mid == (len(xs)-1) or x > xs[mid+1]:
                return mid
            else:
                return search2(mid + 1, right)
        if left == right:
            return None
        if xs[mid] > x:
            return search2(mid + 1, right)
        if x > xs[mid]:
            return search2(left, mid-1)
    
    if xs == []:
        return 0
    first_search = search1(left, right)
    second_search = search2(left, right)
    
    if first_search == None or second_search == None:
        return 0
    else:
        return second_search - first_search + 1


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    
    low = lo
    high = hi
    def search(low, high):
        m1 = low + (high - low)/10
        m2 = low + (high- low)/5
        if high - low < epsilon:
            return high
        if f(m1) > f(m2):
            return search(m1, high)
        if f(m1) < f(m2):
            return search(low, m2)
    
    return search(low,high)

# collaborated with Yusuf Ismaeel
