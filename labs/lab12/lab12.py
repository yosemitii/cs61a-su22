import re


def link_pop(lnk, index=-1):
    '''Implement the pop method for a Linked List.
    
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> removed = link_pop(lnk)
    >>> print(removed)
    5
    >>> print(lnk)
    <1 2 3 4>
    >>> link_pop(lnk, 2)
    3
    >>> print(lnk)
    <1 2 4>
    >>> link_pop(lnk)
    4
    >>> link_pop(lnk)
    2
    >>> print(lnk)
    <1>
    '''
    if index == -1:
        while lnk.rest.rest != Link.empty:
            lnk = lnk.rest
        removed = lnk.rest.first
        lnk.rest = Link.empty
    else:
        while index > 0:
            ptr = lnk
            lnk = lnk.rest
            index -= 1
        removed = lnk.first
        ptr.rest = lnk.rest
    return removed


def prune_min(t):
    """Prune the tree mutatively.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    if t.is_leaf():
        return
    to_remove = t.branches[1]
    t.branches.remove(to_remove)
    # if t.is_leaf():
    #     return
    # else:
    prune_min(t.branches[0])
    #     _____________
    return  # return statement to block alternate from running


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"


def add_trees(t1, t2):
    """
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print(add_trees(Tree(2), Tree(3, [Tree(4), Tree(5)])))
    5
      4
      5
    >>> print(add_trees(Tree(2, [Tree(3)]), Tree(2, [Tree(3), Tree(4)])))
    4
      6
      4
    >>> print(add_trees(Tree(2, [Tree(3, [Tree(4), Tree(5)])]), \
    Tree(2, [Tree(3, [Tree(4)]), Tree(5)])))
    4
      6
        8
        5
      5
    """
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    new_label = t1.label + t2.label
    t1_branches, t2_branches = t1.branches, t2.branches
    length_t1, length_t2 = len(t1_branches), len(t2_branches)
    if length_t1 >= length_t2:
        new_branches = [add_trees(t1_branches[i], t2_branches[i]) for i in range(length_t2)] + t1_branches[length_t2: length_t1]
    elif length_t1 < length_t2:
        new_branches = [add_trees(t1_branches[i], t2_branches[i]) for i in range(min(length_t1, length_t2))] \
                       + t2_branches[min(length_t2,length_t1): max(length_t2,length_t1)]
    return Tree(new_label, new_branches)


def address_oneline(text):
    """
    Finds and returns if there are expressions in text that represent the first line
    of a US mailing address.

    >>> address_oneline("110 Sproul Hall, Berkeley, CA 94720")
    True
    >>> address_oneline("What's at 39177 Farwell Dr? Is there a 39177 Nearwell Dr?")
    True
    >>> address_oneline("I just landed at 780 N McDonnell Rd, and I need to get to 1880-ish University Avenue. Help!")
    True
    >>> address_oneline("123 Le Roy Ave")
    True
    >>> address_oneline("110 Unabbreviated Boulevard")
    False
    >>> address_oneline("790 lowercase St")
    False
    """
    block_number = r'\d+'
    # cardinal_dir = r'(\s[NSWE])?'  # whitespace is important!
    cardinal_dir = r'([NSWE])?'  # whitespace is important!
    # street = r'\s[A-Z]{1}[a-z]+'
    street = r'(\s[A-Z]{1}[A-Za-z]+)+'
    # street = r''
    # type_abbr = r'\s(Dr)?(Hall)?(Ave)?(St)?'
    type_abbr = r'\s(Dr|Hall|Ave|St|Rd)'
    # type_abbr = r''
    street_name = f"{cardinal_dir}{street}{type_abbr}"
    print("DEBUG: ", f"{block_number} {street_name}")
    # return bool(re.search(f"{block_number} {street_name}", text))
    return bool(re.search(r'\d+(\s[NSWE])?(\s[A-Z]{1}[A-Za-z]+)+\s(Dr|Hall|Ave|St|Rd)', text))


def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]

    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random


random = make_test_random()

# Phase 1: The Player Class


class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135

    """

    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"
        threshold = max(0.1, self.popularity / (self.popularity + other.popularity))
        if random() < threshold:
            self.popularity += 50
            # other.popularity -= 50
        else:
            self.popularity -= 50
            # other.popularity += 50
        if self.popularity < 0:
            self.popularity = 0
        if other.popularity < 0:
            other.popularity = 0


    def speech(self, other):
        "*** YOUR CODE HERE ***"
        self.votes += self.popularity // 10
        self.popularity += self.popularity // 10
        other.popularity -= other.popularity // 10
        if other.popularity < 0:
            other.popularity = 0

    def choose(self, other):
        return self.speech


# Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            "*** YOUR CODE HERE ***"
            self.turn += 1
            print("DEBUG: ", self.winner)
            if self.turn % 2 == 1:
                self.p1.choose(self.p2)
            else:
                self.p2.choose(self.p1)
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        "*** YOUR CODE HERE ***"
        if self.p1.votes >= self.p2.votes:
            return self.p1
        elif self.p1.votes > self.p2.votes:
            return self.p2
        # else:
        #     return None


# Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity <= other.popularity:
            return self.debate
        else:
            return self.speech


class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False

    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        print("DEBUG: ", self.popularity == 0)
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech




def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    elements = []
    elem_dict = {}
    "*** YOUR CODE HERE ***"
    for lst in lst_of_lsts:
        this_lst = []
        for elem in lst:
            print("DEBUG: THIS LST", this_lst, " elem: ", elem)
            if elem not in this_lst:
                if elem not in elem_dict:
                    elem_dict[elem] = 1
                else:
                    elem_dict[elem] += 1
                this_lst.append(elem)
    for index in elem_dict:
        if elem_dict[index] == len(lst_of_lsts):
            elements.append(index)
    return elements


def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    # return [[x for x in suits].append(y) for y in ranks]
    return [[x, y] for x in suits for y in ranks]

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
