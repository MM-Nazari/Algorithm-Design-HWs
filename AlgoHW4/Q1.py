def generate_fraction_code(n):
    if n == 1:
        return "1"
    elif n == 2:
        return "1+\\frac{2}{3}"
    else:
        base = generate_base(n)
        numerator = generate_numerator(n)
        denominator = generate_denominator(n)
        return f"{base}+\\frac{{{numerator}}}{{{denominator}}}"


def generate_base(n):
    return str(n)


def generate_numerator(n):
    if n == 2:
        return str(2)
    else:
        base = generate_base(2)
        numerator = generate_numerator(n-1)
        denominator = generate_denominator(n-1)
        return f"{base}+\\frac{{{numerator}}}{{{denominator}}}"


def generate_denominator(n):
    if n == 2:
        return str(3)
    else:
        for i in range(3, n+1):
            base = generate_base(i)
            numerator = generate_numerator(n-1)
            denominator = generate_denominator(n-1)
            return f"{base}+\\frac{{{numerator}}}{{{denominator}}}"


n = int(input())
print(generate_fraction_code(n))
