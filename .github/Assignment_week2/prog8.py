
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
middle_index = len(prime_numbers) // 2
middle_elements = prime_numbers[middle_index - 2: middle_index + 3]
print(middle_elements)
everysecond_element = []
for i in range(0, len(prime_numbers), 2):
    everysecond_element.append(prime_numbers[i])
print(everysecond_element)
lastthree = prime_numbers[-3:]
print(lastthree)
reversed = prime_numbers[::-1]
print(reversed)
desclist = sorted(prime_numbers, reverse=True)
print(desclist)