def knapsack_dp(capacity, weights, values, n):
    """takes two lists of weight and values and tries to optimize based on the capasity, capasity referes to the weight

        Args:
            capacity (int): weight capacity
            weights (list): how much the item of index x is weighted
            values (list): the value of item of index x
            n (int): number of item indexes

        Returns:
            _type_: optimal solution
        """
    grid = [[0 for x in range(capacity + 1)]
            for x in range(n + 1)]

    for item in range(n + 1):
        for cap in range(capacity + 1):

            if item == 0 or cap == 0:
                grid[item][cap] = 0

            elif weights[item - 1] <= cap:
                grid[item][cap] = max(values[item - 1] +
                                grid[item - 1][cap - weights[item - 1]],
                                grid[item - 1][cap])
            
            else:
                grid[item][cap] = grid[item - 1][cap]

    return grid[n][capacity]

item_val = [200, 150, 100, 50]
item_wt = [40, 32, 16, 8]
total_cap = 64
n_items = len(item_val)

print('Max value to put in kanpsack of capacity W:', total_cap)
print(knapsack_dp(total_cap, item_wt, item_val, n_items), '$')