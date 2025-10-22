
num1 = int(input('Informe o primeiro número: ').strip())
num2 = int(input('Informe o segundo número: ').strip())
num3 = int(input('Informe o terceiro número: ').strip())

setNum = [num1, num2, num3]
setNum.sort()

print('O maior número é {} e o menor é {}' .format(setNum[0], setNum[2]))

### Alternative way using if, elif, else

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else: # num3 é o menor
    if num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)