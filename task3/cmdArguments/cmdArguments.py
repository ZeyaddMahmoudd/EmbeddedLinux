import sys

n = len(sys.argv)

print("Number of arguments : {n}")

print("Argument List : [", end = "")

for i in range(1, n):
    print(f"{sys.argv[i]}", end = "")
    if i != n-1:
        print(", ", end = "")

print("]")