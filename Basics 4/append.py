import array as arr
numbers = arr.array('i', [10, 20, 30, 40])
print(numbers[1])
numbers.append(50)
numbers.insert(1, 15)
last_item = numbers.pop()
numbers.reverse()

for num in numbers:
    print(num)
