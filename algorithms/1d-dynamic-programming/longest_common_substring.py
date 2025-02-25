def memo_llcs(A, B):
    n = len(A)
    m = len(B)

    # Create a 2-dimensional array Soln and initialize all elements to None
    Soln = [[None] * (m + 1) for _ in range(n + 1)]

    # Call the helper function to compute the LLCS
    return memo_helper(A, B, n, m, Soln)

def memo_helper(A, B, i, j, Soln):
    # Check if the solution is already computed
    if Soln[i][j] is None:
        # Base case: if i or j is 0, LLCS is 0
        if i == 0 or j == 0:
            Soln[i][j] = 0
        # If the characters match, compute LLCS based on the subproblem
        elif A[i - 1] == B[j - 1]:
            Soln[i][j] = memo_helper(A, B, i - 1, j - 1, Soln) + 1
        # If characters don't match, choose the maximum of the two subproblems
        else:
            Soln[i][j] = max(memo_helper(A, B, i - 1, j, Soln), memo_helper(A, B, i, j - 1, Soln))

    # Return the computed LLCS for the current subproblem
    return Soln[i][j]


# Example usage:
A = "tycoon"
B = "country"
result = memo_llcs(A, B)
print("Length of Longest Common Subsequence:", result)

