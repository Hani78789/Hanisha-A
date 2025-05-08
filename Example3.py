# odd number series
def generate_odd_series(a):
    if a % 2 == 0:
        a -= 1

    result = []
    for i in range(1, 2 * a, 2):
        result.append(i)

    print(", ".join(map(str, result)))

# Example
generate_odd_series(6)
# Output: 1, 3, 5, 7, 9
