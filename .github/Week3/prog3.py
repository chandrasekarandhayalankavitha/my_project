
# Write operation
with open("report.txt", "w") as file:
    file.write("TestCase1 - Passed\n")
    file.write("TestCase2 - Failed\n")
    file.write("TestCase3 - Passed\n")

# Append operation
with open("report.txt", "a") as file:
    file.write("TestCase4 - Passed\n")
    file.write("TestCase5 - Failed\n")

TotalTests = 0
Passed = 0
Failed = 0

with open("report.txt", "r") as file:
    for i in file:
        print(i.strip())
        TotalTests += 1
        if "Passed" in i:
            Passed += 1
        elif "Failed" in i:
            Failed += 1

print("Total Test Cases:", TotalTests)
print("Passed:", Passed)
print("Failed:", Failed)