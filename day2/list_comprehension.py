# lambda example
test_list = list(map(lambda x: x + 10, [1, 2, 3]))
print(test_list)

# list comprehension example
test_list_comprehension = [n * 2 for n in range(0, 10) if n % 2 == 1]
print(test_list_comprehension)

# normal expression example
a = []
for n in range(0, 10):
    if n % 2 == 1:
        a.append(n * 2)
print(a)

# dictionary comprehension

original = {
    '1': 1,
    '2': 2
}
test_dict = {key: value for key, value in original.items()}
print(test_dict)