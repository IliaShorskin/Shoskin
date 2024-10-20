numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = numbers
del(a[4])
b = round(sum(a)/(len(numbers)+1),2)
numbers.insert(4,b)

print("Измененный список:", numbers)