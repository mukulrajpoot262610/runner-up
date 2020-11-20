# This program is to find 2nd position people.

# n = int(input("Enter how many stduents: "))

# lst = []

# for i in range(0,n):
#     score = int(input(f"Enter {i+1} score: "))
#     lst.append(f"{score}")

# m = max(lst)
# m = int(m)
# lst2 = []

# for d in lst:
#     d = int(d)
#     if d == m:
#         pass
#     else:
#         lst2.append(d/m)

# n = max(lst2)
# ans = n * m
# print(int(ans))

# Attept 2

# n = int(input("Enter how many stduents: "))

# lst = []

# for i in range(0,n):
#     score = int(input(f"Enter {i+1} score: "))
#     lst.append(f"{score}")

# m = max(lst)

# lst2 = []

# for d in lst:
#     if d == m:
#         pass
#     else:
#         lst2.append(d)

# n = max(lst2)
# print(n)

# Attempt 3

n = int(input("Enter how many stduents: "))

lst = []

for i in range(0,n):
    score = int(input(f"Enter {i+1} score: "))
    lst.append(f"{score}")

m = max(lst)

lst.remove(m)

n = max(lst)
print(n)
input()