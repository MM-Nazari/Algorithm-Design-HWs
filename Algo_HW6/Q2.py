def calculate_blankets_needed(n, d, animals):
    # Sort the sleeping positions of animals
    animals.sort()

    # Initialize the number of blankets needed
    blankets_needed = 1

    # Initialize the rightmost position covered by the first blanket
    rightmost_covered = animals[0] + d

    # Iterate over the sleeping positions of animals
    for i in range(1, n):
        # If the animal's sleeping position is not covered by the current blanket
        if animals[i] > rightmost_covered:
            # Increment the number of blankets needed
            blankets_needed += 1
            # Update the rightmost position covered by the new blanket
            rightmost_covered = animals[i] + d

    return blankets_needed


# Read input
n, d = map(int, input().split())
animals = list(map(int, input().split()))

# Calculate and print the minimum number of blankets needed
print(calculate_blankets_needed(n, d, animals))
