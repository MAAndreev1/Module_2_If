x = 38

print("Дратути!")
if x <  0:
    print('Меньше нуля')
print("Досвидания!")

# примеры

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > b or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')

# что нельзя сравнивать - разные типы

# if '6' > 5:
#     print('успех')
#
# if [5, 6] > 5:
#     print('успех')

# но

if '6' != 5:
    print('успех "6" != 5')