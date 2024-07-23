def generate_latex_fraction(n):
    if n == 1:
        return "1"
    else:
        a, b = calculate_ab(n)
        prev_fraction = generate_latex_fraction(n - 1)
        return f"{prev_fraction}+\\frac{{{a}}}{{{b}}}"

def calculate_ab(n):

    a = 2 ** (n-1)
    b = 2 ** (n)

    return a, b

def main():
    n = int(input())
    print(generate_latex_fraction(n))

if __name__ == "__main__":
    main()
