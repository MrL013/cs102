'''Calculator'''

def calculator(num1, operator, num2):
    '''Function for calculate'''
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b
    }

    if operator in operators:
        result = operators[operator](num1, num2)
        return round(result, 2)

    return False

try:
    print('Введите операцию в формате "2 + 2" используя операторы (-, +, *, /, //, %)')
    exp = input().split()
    n1 = float(exp[0])
    op = exp[1]
    n2 = float(exp[2])
    result = calculator(n1, op, n2)
    print(result)
except:
    print('Что-то пошло не так, проверьте корректность ввода!')