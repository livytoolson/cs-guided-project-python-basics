#     0   1   2   3
a = [11, 22, 33, 44]

# print(a[2]) # bring one element out of lsit

# a[2] = 999 # reasign value at index 2

# Slicing a list --> ALWAYS creates a new list
print(a[1:3]) # creates a new list that has everything from index 1 to index 2
print(a[1:]) # creates a new list from index 1 to the end
print(a[:2]) # creates a new list from beginning of list up to index 2
print(a[:]) # makes a copy of the entire list

for num in a:
    print(num)

print() # prints a blank line

for i, num in enumerate(a):
    # print(i, num)
    print(f"Index {i} holds the value: {num}.")

print()

# len tells you how many elements are in a particular list
for i in range(len(a)):
    elem = a[i]
    print(f"Index {i} holds the value: {num}.")