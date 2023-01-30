def get_op():
    op = int(input('1 - добавить студента, 2 - добавить предмет, 3 - добавить оценку, 4 - показать список, 5 - показать конкретный список, 6 - выход'))
    return op

def input_student():
    name = input('Введите имя и фамилию студента: ')
    return name

def input_less():
    less = input('Введите назавание предмета: ')
    return less

def input_mark():
    name = input('Введите имя студента: ')
    less = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, less, mark

def get_name_to_show():
    name = input("Введите имя для просмотра оценки: ")
    return name
