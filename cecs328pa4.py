def cargo(crates, T, W, D):
    # Initialize a 3D DP array filled with zeros
    dp = [[[0] * (D + 1) for _ in range(W + 1)] for __ in range(T + 1)]

    # Helper function to count toasters, washers, and dryers in a crate
    def count_items(crate):
        return crate.count('t'), crate.count('w'), crate.count('d')

    # Process each crate to update the DP table
    for crate in crates:
        t_count, w_count, d_count = count_items(crate)
        # Iterate over possible counts of items from maximum down to item counts in the crate
        for t in range(T, t_count - 1, -1):
            for w in range(W, w_count - 1, -1):
                for d in range(D, d_count - 1, -1):
                    # Update the DP table to reflect the maximum crates that can be taken
                    dp[t][w][d] = max(dp[t][w][d], dp[t - t_count][w - w_count][d - d_count] + 1)

    # The final value at dp[T][W][D] will give us the maximum number of crates that can be taken
    return dp[T][W][D]