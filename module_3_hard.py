# Дополнительное практическое задание по модулю "Подробнее о функциях."

# x = [1, 2, 3]
# print(type(x))
# y =  {'a': 4, 'b': 5}
# print(type(y))
# z = (6, {'cube': 7, 'drum': 8}),
# print(type(z))
# v = "Hello",
# print(type(v))
# b = ((), [{(2, 'Urban', ('Urban2', 35))}])
# print(type(b))

data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]


def calculate_structure_sum(data_structure):
    summa = 0
    if data_structure == []:
        return summa
    if isinstance(data_structure, dict):  # print('dict', data_structure)

        for key, value in data_structure.items():  # print(summa) print(key, value)
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)


    elif isinstance(data_structure, (tuple, set, list)):  # print('List, tuple, set', data_structure)

        for i in data_structure:
            summa += calculate_structure_sum(i)  # print(i)

    elif isinstance(data_structure, (int, float)):  # print('int, float', data_structure)

        summa += data_structure
    elif isinstance(data_structure, str):  # print('str', data_structure)

        summa += len(data_structure)
    return summa


result = calculate_structure_sum(data_structure)
print(result)
