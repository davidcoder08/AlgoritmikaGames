print('Добрый день!')
print('Давате узнаем что же больше!')
action = input('Что вы будете делать?')


if action == 'складывать':
    firstnumber = plus_result
    first = int(input('Введите первое число!'))
    second = int(input('Введите второе число!'))
    plus_result = first + second
    action2 = input('Что вы будете делать дальше?')


if action == 'вычитать':
    firstnumber = minus_result
    first1 = int(input('Введите первое число!'))
    second1 = int(input('Введите второе число!'))
    minus_result = first1 + second1
    action2 = input('Что вы будете делать дальше?')


if action == 'умножать':
    firstnumber = umnojat_result
    first2 = int(input('Введите первое число!'))
    second2 = int(input('Введите второе число!'))
    umnojat_result = first2 + second2
    action2 = input('Что вы будете делать дальше?')


delit_result = firstnumber / secondnumber
if action == 'делить':
    firstnumber = delit_result
    first3 = int(input('Введите первое число!'))
    second3 = int(input('Введите второе число!'))
    delit_result = first3 + second3
    action2 = input('Что вы будете делать дальше?')




