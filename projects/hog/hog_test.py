import hog
import dice
# dice1 = dice.make_test_dice(3, 1, 2, 2, 5, 6, 6, 4, 6)
# always = hog.always_roll
# s0, s1 = hog.play(always(9), always(9), 3, 3, goal=5, dice=dice1)

# leader, message = hog.announce_lead_changes(5, 0)

from hog import play, always_roll, announce_lead_changes, both
from dice import make_test_dice
def count(n):
    def say(s0, s1, curr_count=None):
        if curr_count is None:
          curr_count = n
        return curr_count + 1, str(curr_count) + " " + str(s0)
    return say
# s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))

def echo(s0, s1, player=None):
    return player, str(s0) + " " + str(s1)

strat0 = lambda score, opponent: 1 - opponent // 10
strat1 = always_roll(3)
# s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)

def total(s0, s1, player=None):
    return player, str(s0 + s1)
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)

def echo_0(s0, s1, player=None):
    return player, f"* {s0}" # message of the form: "* s0"
def echo_1(s0, s1, player=None):
    return player, f"** {s1}" # message of the form: "** s1"

s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))

dice = hog.make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
a = hog.max_scoring_num_rolls(dice, total_samples=1000)

hog.pigs_on_prime_strategy(78, 14, 13, 6)