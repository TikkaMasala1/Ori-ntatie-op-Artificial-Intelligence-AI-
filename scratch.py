def mean(lst):
    avg = sum(lst) / len(lst)
    return float(avg)


lst = [4, 2, 5, 8, 6]
squaredList = []
avg = mean(lst)

for x in lst:
    squaredList.append(pow(x - avg, 2))

variantie = sum(squaredList) / len(squaredList)
print(variantie)
