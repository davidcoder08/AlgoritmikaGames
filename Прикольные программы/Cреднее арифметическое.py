numbers = int(input('Введите число:'))
result = []
while numbers > 0:
   result.append(numbers)
   numbers = int(input('Введите число (для остановки напишите отрицательное число)'))
print(sum(result) / len(result))