n = list(map(int, input("Enter the elements separated by spaces: ").split()))
positive_values = [x for x in n if x > 0]
print(positive_values)
