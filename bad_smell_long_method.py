# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    # Чтение данных из строки
    data = _read(csv)
    data = _sort(data)
    data = filter_func(data)
    return data


def _read(csv):
    return [x.split(';') for x in csv.split('\n')]


def _sort(data):
    # Сортировка по возрасту по возрастанию
    return sorted(data, key=lambda age: int(age[1]))


def filter_func(new_data):
    # Фильтрация
    result = [person for person in new_data if int(person[1]) < 30]
    return result


if __name__ == '__main__':
    print(get_users_list())
