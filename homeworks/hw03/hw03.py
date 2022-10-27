HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"

    if pos == 8:
        return 1
    elif pos == 0:
        return 0
    elif pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return 0 + num_eights(pos // 10)



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(num, step):
        print("DEBUG:", num, step)
        if num == n:
            return 1
        if num_eights(num) == 0 and num % 8 != 0:
            return step + helper(num + 1, step)
        elif num_eights(num) != 0 or num % 8 == 0:
            return -step + helper(num + 1, -step)
    return helper(1, 1)



def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    # def helper(n):
    #     print("DEBUG", n)
    #     if n < 4:
    #         return 1
    #     elif n >= 5 and n <10:
    #         return 2 * helper(n - 5)
    #     elif n >= 10 and n < 25:
    #         return 4 * helper(n - 10)
    #     elif n >= 25:
    #         return 12 * helper(n - 25)
    # return helper(change)
    def helper(n, max_coin):
        print("DEBUG", n, max_coin)
        if n == 0 or max_coin == 1:
            return 1
        # elif n < 0:
        #     return 0
        elif max_coin != 1 and n < max_coin:
            return helper(n, get_smaller_coin(max_coin))
        # elif max_coin == 1:
        #     return helper(n-max_coin, max_coin)
        else:
            return helper(n - max_coin, max_coin) + helper(n, get_smaller_coin(max_coin))
    return helper(change, 25)

