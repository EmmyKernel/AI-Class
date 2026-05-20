employees = [
    "Emmanuel", "Tintin", "John", "David", "Mabel","Frank", "Grace", "Henry", "Mark", "Mary"
]

subList1 = employees[:5]
subList2 = employees[5:]

subList2.append("Kriti Brown")
print("subList2 after append: ", subList2)

del(subList1[1])
print("subList1 after removal: ", subList1)

subList1.extend(subList2)
mergedList = subList1
print("Merged list: ", mergedList)

salaryList = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
print("Salary list: ", salaryList)

for s in salaryList:
    salaryList = s * 1.04
    print(salaryList)

    