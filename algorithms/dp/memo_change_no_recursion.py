def memo_change_helper(n):
    if n <= 0:
        return []

    memo = {0: []}  # Initialize memo[0] with an empty list
    for i in range(1, n + 1):
        change = []

        if i >= 25 and (i - 25 not in memo or len(memo[i - 25]) > 0):
            change = memo[i - 25] + ["quarter"]
        elif i >= 10 and (i - 10 not in memo or len(memo[i - 10]) > 0):
            change = memo[i - 10] + ["dime"]
        elif i >= 5 and (i - 5 not in memo or len(memo[i - 5]) > 0):
            change = memo[i - 5] + ["nickel"]
        elif i >= 1:
            if (i - 1 not in memo) or (i - 1 in memo and len(memo[i - 1]) > 0):
                change = memo[i - 1] + ["penny"]

        memo[i] = change

    return memo[n]

# Example usage:
n = 37
result = memo_change_helper(n)
print(result)

