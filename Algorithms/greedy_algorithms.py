# The paradigm behind the greedy concept is that it builds up a solution piece by piece,
# always choosing the next piece that offers the most obvious and immediate benefit.
# By using several iterations, and by obtaining the best result, at a certain iteration
# the result should be computed. In other words, it follows the problem solving method of
# making the locally optimum choice at each stage with the hope of finding the global optimum.
#
# Basic- Mice In The Hole
# Advanced- Fractional Knapsack
# Mindbreaker- Egyptian Fractions (Fibonacci)

# ________________________________________________EXAMPLES__________________________________________________________

# BASIC - MICE IN HOLES

# Returns minimum time required to place mice in holes using the Greedy approach. We can put every mouse
# to its nearest hole to minimize the time. This can be done by sorting the positions of mice and holes.

def assignHole(mice, holes):
    # Base - num of mice and holes should be the same
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"
    # Sort first
    mice.sort()
    holes.sort()

    # Finding max difference between ith mice and hole
    max_diff = 0
    min_l = []

    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])
        if abs(mice[i] - holes[i]) <= 0:
            min_diff = 0
        else:
            min_l.append(abs(mice[i] - holes[i]))
            min_diff = min(min_l)

    return max_diff, min_diff


mice = [3, -4, 2,-6]
# Hole positions
holes = [4, 0, 5, 0]

# The required answer is returned from the function
min_time, min_pos = assignHole(mice, holes)
print("The last mouse gets into the hole in time:", min_time, min_pos)


# ______________________________________________________________________

# ADVANCED: FRACTIONAL KNAPSACK
def fractional_knapsack(value, weight, capacity):
    items = list(range(len(value)))
    print(items)
    ratio = [v//w for v, w in zip(value, weight)]
    print(ratio)
    srt_ratios = sorted(ratio, reverse=False)
    print(srt_ratios)
    items.sort(key=lambda i: ratio[i], reverse=False)
    print(items)

    max_value = 0
    fractions = [0] * len(value)
    print(fractions)
    for i in items:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
            print(max_value)
        else:
            fractions[i] = capacity // weight[i]
            max_value += value[i] * capacity // weight[i]

    return max_value

weight = [30, 50, 10, 70, 40]
value = [150, 100, 90, 140, 120]
capacity = 150

print(fractional_knapsack(value, weight, capacity))
