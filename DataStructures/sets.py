E = set(map(int, input("Enter the elements of set E separated by spaces: ").split()))
N = set(map(int, input("Enter the elements of set N separated by spaces: ").split()))

union_set = E.union(N)
intersection_set = E.intersection(N)
difference_set = E.difference(N)
symmetric_difference_set = E.symmetric_difference(N)

print("Union of E and N is", union_set)
print("Intersection of E and N is", intersection_set)
print("Difference of E and N is", difference_set)
print("Symmetric difference of E and N is", symmetric_difference_set)
