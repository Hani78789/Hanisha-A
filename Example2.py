# generate odd number series
def generate_odd_series(number):
    result = []
    for i in range(number):
        result.append(i * 2 + 1)
    return result

# Example usage
print(generate_odd_series(4))
# ouput [1, 3, 5, 7]
