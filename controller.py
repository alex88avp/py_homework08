import view

main_dct = {}
students = []
lessons = []

def start():
    while True:
        op = view.get_op()
        if op == 1:
            student = view.input_student()
            main_dct[student] = {}
            students.append(student)
            if lessons:
                for less in lessons:
                    main_dct[student][less] = []
        elif op == 2:
            less = view.input_less()
            lessons.append(less)
            for name in students:
                main_dct[name][less] = []
        elif op == 3:
            name, less, mark = view.input_mark()
            main_dct[name][less].append(mark)
        elif op == 4:
            print(main_dct)
        elif op == 5:
            name = view.get_name_to_show()
            print(main_dct[name])
        elif op == 6:
            break
        print(main_dct)

