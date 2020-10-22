weights = [4, 5, 3]
values = [11, 12, 7]

def knapsack(capacity, weights, values, n):
    """given knapsack of `capacity`, n items with weights and values,
    ﬁnd the most valuable selection of items that will ﬁt in the knapsack.

    Parameters
    ----------
    capacity : int
        capacity of the bag
    weights : list of ints
        weights of each item
    values : list of ints
        values of each item
    n : int
        total number of items

    Returns
    -------
    int
        the largest value that can be put in a bag of `capacity`
    """
    V = {0: 0}
    for w in range(1, capacity + 1):
        V[w] = 0
        for i in range(0, n):
            if weights[i] <= w and (V[w - weights[i]] + values[i]) > V[w]:
                V[w] = V[w - weights[i]] + values[i]

    return V[capacity]


print(knapsack(10, weights, values, 3))
