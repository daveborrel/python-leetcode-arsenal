def Soln_prime(i, Soln):
    if i < 0:
        return float('inf')
    elif i == 0:
        return 0
    else:
        return Soln[i]

def DP_Change(n):
    if n <= 0:
        return Soln_prime(n, [])
    else:
        # Assumes n > 0; otherwise, just run Soln_prime
        Soln = [0] * (n + 1)
        for i in range(1, n + 1):
            Soln[i] = min(Soln_prime(i - 25, Soln) + 1, Soln_prime(i - 10, Soln) + 1, Soln_prime(i - 1, Soln) + 1)
        return Soln[n]

# Example usage:
result = DP_Change(47)
print(result)










    

    