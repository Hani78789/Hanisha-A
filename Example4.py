#count multiples of 1 to 9 in an arry
def count_multiples(arr):
    count = {}
    for i in range(1, 10):
        count[i] = 0
        for num in arr:
            if num % i == 0:
                count[i] += 1
    return count

# Example:
input_array = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(input_array))
#{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
