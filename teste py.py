array1 = [1,10,2,2,10,3,3,3,4,5,5]
arrayNoRepeat = []

for n in array1:
    if n not in arrayNoRepeat:
        arrayNoRepeat.append(n)
    
print(arrayNoRepeat)

