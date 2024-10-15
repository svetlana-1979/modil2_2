from traceback import print_exc

first = int(input ('введите число first '))
second = int (input ('введите число second '))
third = int (input ('введите число third '))
print(first)
print(second)
print(third)
if first != second and first != third and second != third:
    print(0)
elif first == second and third:
    print(3)
elif first == second or third:
    print (2)
elif second == third or first:
    print(2)
