
l = ["Alice", "Bob", "Charlie", "David", "Eve"]
l.sort()
for i in range(1, len(l)+1):
    print(i,end="")
    print(".",l[i-1])