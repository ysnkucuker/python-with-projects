# This program finds all Pythagorean triples (a, b, c)
# where a² + b² = c² and 1 ≤ a ≤ b ≤ c ≤ 100.
# Example: (3, 4, 5)

def pythagorean_triples(limit: int = 100) -> None:
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):   # start from 'a' to avoid duplicates
            for c in range(b, limit + 1):
                if a * a + b * b == c * c:
                    print(f"a={a}, b={b}, c={c}")


pythagorean_triples()
