import random
min_elements = 3
max_elements = 10
num_elements = random.randint(min_elements, max_elements)
numbers = []
for j in range(num_elements):
    numbers.append(random.randint(1, 10))
print(numbers)
numbers_copy = numbers.copy()
list = [numbers_copy[0], numbers_copy[2], numbers_copy[-2]]
print(list)
