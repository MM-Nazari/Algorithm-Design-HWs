# Function to generate LaTeX-formatted fraction sequence for a given n
def generate_fraction(n):
    if n == 1:
        return "1"
    elif n == 2:
        return "1+\\frac{2}{3}"
    else:
        numerator = ""
        denominator = ""
        for i in range(1, n + 1):
            numerator += str(2 ** (i - 1))
            denominator += str(2 ** i - 1)
            if i != n:
                numerator += "+"
                denominator += "+"
        return f"1+\\frac{{{numerator}}}{{{denominator}}}"

# Generate and print LaTeX-formatted fractions for n = 10 and n = 11
n_10 = generate_fraction(10)
n_11 = generate_fraction(11)

print("For n = 10:")
print(n_10)
print()

print("For n = 11:")
print(n_11)
