def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    # count = 0
    # digit = 0
    # for num in t:
    #     if num == x:
    #         count +=1
    #     digit += 1
    #     if digit == n:
    #         return count
    # return count

    # ========SOLUTION 2===================
    # length = min(len(t), n)
    count = 0
    num = next(t) for _ in range(n):
        if num == x:
            count += 1
    return count
    "*** YOUR CODE HERE ***"


def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale([1, 2, 3, 4, 5, 6, 7, 8], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while i < len(it):
        yield it[i] * multiplier
        i += 1



def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i > 1:
        if i % 2 == 0:
            yield i
            i //= 2
        else:
            yield i
            i = i*3 + 1
    if i == 1:
        yield 1

