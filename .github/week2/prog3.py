
marks = [78, 85, 62, 90, 55, 88]
print("highest marks:", max(marks))
print("lowest marks:", min(marks))
print("average marks:", sum(marks)/len(marks))
for i in range(len(marks)):
    if marks[i] > 75:
        print(marks[i])
marks.append(95)
print(marks)
marks.remove(55)
print(marks)
marks.sort()
print(marks)
