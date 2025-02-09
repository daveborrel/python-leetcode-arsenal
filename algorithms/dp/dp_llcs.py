def DP_LLCS(A, B):
    n = len(A)
    m = len(B)

    # Create a 2-dimensional array for the table
    Soln = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in the base cases
    for i in range(n + 1):
        Soln[i][0] = 0

    for j in range(1, m + 1):
        Soln[0][j] = 0

    # Fill in the recursive cases column-by-column, top-to-bottom
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                Soln[i][j] = Soln[i - 1][j - 1] + 1
            else:
                Soln[i][j] = max(Soln[i - 1][j], Soln[i][j - 1])

    # Return the length of the LCS
    return Soln[n][m]

# Example usage:
A = "kitten"
B = "sitting"
result = DP_LLCS(A, B)
print("Length of Longest Common Subsequence:", result)