students = [
    {'Фамилия': "Иванов", 'Имя': 'Иван', 'Отчество': 'Иванович', 'Год рождения': 2003, 'Курс': 1, 'Группа': '219-1',
     'Оценки': {'ООП': 4, 'БД': 3, 'Экология': 5, 'Химия': 2, 'История': 5}},
    {'Фамилия': "Петров", 'Имя': 'Петр', 'Отчество': 'Петрович', 'Год рождения': 2001, 'Курс': 1, 'Группа': '219-1',
     'Оценки': {'ООП': 3, 'БД': 2, 'Экология': 1, 'Химия': 5, 'История': 4}},
    {'Фамилия': "Денисов", 'Имя': 'Денис', 'Отчество': 'Денисович', 'Год рождения': 2001, 'Курс': 1,
     'Группа': '219-2',
     'Оценки': {'ООП': 3, 'БД': 5, 'Экология': 5, 'Химия': 5, 'История': 5}},
    {'Фамилия': "Алексеев", 'Имя': 'Алексей', 'Отчество': 'Алексеевич', 'Год рождения': 2002, 'Курс': 2,
     'Группа': '219-1',
     'Оценки': {'ООП': 3, 'БД': 2, 'Экология': 5, 'Химия': 5, 'История': 3}},
    {'Фамилия': "Сергеев", 'Имя': 'Сергей', 'Отчество': 'Сергеевич', 'Год рождения': 2002, 'Курс': 3,
     'Группа': '219-2',
     'Оценки': {'ООП': 3, 'БД': 2, 'Экология': 4, 'Химия': 5, 'История': 1}}
]


def sorted_course(students):
    import operator
    sorted_dict = sorted(students, key=operator.itemgetter('Курс', 'Фамилия'))

    return sorted_dict


# print(*sorted_course(students),sep = "\n")


def get_groups_marks(students):
    from collections import defaultdict
    from statistics import mean

    result = {}
    for student in students:
        group = student['Группа']
        marks = student['Оценки']
        if (group in result):
            result[group].append(marks)
        else:
            result[group] = [marks]
    for gr in result:
        r = defaultdict(list)
        [r[c].append(cl[c]) for cl in result[gr] for c in cl]
        print(f'средние оценки группы {gr}')
        for k in r:
            print(f'{k}: {mean(r[k]):.2f}')
        print()


# print(get_groups_marks(students))


def vozrast(students):
    x = []
    for student in students:
        x.append(student['Год рождения'])
    list_of_age = set(x)
    for student in students:
        if student['Год рождения'] == min(list_of_age):
            print(f'Самые старшие студенты:{student}')
        elif student['Год рождения'] == max(list_of_age):
            print(f'Самые младшие студенты:{student}')
    return


def best_student(students):
    from statistics import mean

    result = {}
    for student in students:
        name = student['Фамилия']
        for el in [d['Оценки'] for d in students]:
            marks = mean(el.values())
            if name in result:
                result[name].append(marks)
            return result


# print(best_student(students))

def get_groups_marks1(students):
    from statistics import mean
    for student in students:
        marks = mean(student['Оценки'].values())
        student.update({'Оценки': marks})
        result = {}
    for student in students:
        group = student['Группа']
        name_student = student['Оценки'], student['Фамилия']
        if group in result:
            result[group].append(name_student)
        else:
            result[group] = [name_student]
    for key, i in result.items():
        result[key] = max(i)
    print(result)


#print(get_groups_marks1(students))
