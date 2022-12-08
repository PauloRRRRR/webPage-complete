array1 = [1,3,15,11,2]
array2 = [23,127,235,19,8]
arrayDifference = []

for index,n in enumerate(array2):
    if len(array1) == len(array2):
        if n > array1[index]:
            arrayDifference.append(n - (array1[index]))
            
print(arrayDifference)