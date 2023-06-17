# for i in range(0, 4):
#     for j in range(0, i):
#         print(i, end= " ")
#     print()

# for i in range(0, 10):
#     if i%2!=0:
#         for j in range(0, i):
#             print("*", end=" ")
#         print()

# lis = []
# for i in range(0, 10):
#     if i%3!=0:
#         lis.append(i)
#     for i in lis:
#         print(i*"*", end=" ")
#     print()

# k=1
# for i in range(0, 5):
#     for j in range(0, k):
#         print("8", end = " ")
#     print()
#     k += 2

# lis = []
# for i in range(0, 10):
#     if i%2!=0:
#         lis.append(i)
# for i in lis:
#     print(i*"*" + "\n", end=" ",)
number = n = int(input("Enter the Value of n: "))
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()

new_n = n*2
for i in range(1, new_n, +2):
    print("*", end)

