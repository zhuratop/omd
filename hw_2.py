from debugpy.server.cli import switches


def print_departmnet_structure(db):
    departments_db = {}
    for i in range(len(db) - 1):
        if db[i][1] not in departments_db:
            departments_db[db[i][1]] = [db[i][2]]
        else:
            if db[i][2] not in departments_db[db[i][1]]:
                departments_db[db[i][1]].append(db[i][2])

    print()
    for dep in departments_db:
        print(f'Департамент: {dep} \nКоманды: {", ".join(departments_db[dep])} \n')


def dep_review(db, flag_to_print):
    dep_rev_db = {}
    for person in range(len(db) - 1):
        dep = db[person][1]
        salary_person = int(db[person][5])
        if dep not in dep_rev_db.keys():
            dep_rev_db[dep] = {'amount':1, 'min_sal':salary_person, 'max_sal':salary_person, 'avg_sal':salary_person, 'sum_sal':salary_person}
        else:
            dep_rev_db[dep]['amount'] = dep_rev_db[dep]['amount']  + 1
            if salary_person < dep_rev_db[dep]['min_sal']:
                dep_rev_db[dep]['min_sal'] = salary_person
            if salary_person > dep_rev_db[dep]['max_sal']:
                dep_rev_db[dep]['max_sal'] = salary_person
            dep_rev_db[dep]['sum_sal'] += salary_person
    for dep in dep_rev_db.keys():
        dep_rev_db[dep]['avg_sal'] = int(dep_rev_db[dep]['sum_sal'] / dep_rev_db[dep]['amount'])
    if (flag_to_print):
        for dep in dep_rev_db.keys():
            print(f'Департамент: {dep}\n численность: {dep_rev_db[dep]["amount"]} | '
                  f'мин. зп: {dep_rev_db[dep]["min_sal"]} | '
                  f'макс зп: {dep_rev_db[dep]["max_sal"]} | '
                  f'средн. зп: {dep_rev_db[dep]["avg_sal"]}')
            dep_rev_db[dep]['avg_sal'] = int(dep_rev_db[dep]['sum_sal'] / dep_rev_db[dep]['amount'])
    return dep_rev_db


def save_review_to_csv(db, file_name='review_output.csv'):
    reslut_db = dep_review(db, flag_to_print=0)
    dep = list(reslut_db.keys())[0]
    print(reslut_db)
    # print(reslut_db[str(dep)][0])
    try:
        with open(file_name, 'w+', encoding='UTF-8') as file_output:
            columns = ['']
            for key in reslut_db[dep].keys():
                columns.append(key)
            file_output.write(','.join(columns) + '\n')

            for dep in reslut_db.keys():
                row = [dep]
                for metric in reslut_db[dep].values():
                    row.append(str(metric))
                file_output.write(','.join(row) + '\n')
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет доступа к файлу.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    return 0


if __name__ == '__main__':
    # dep_review(database)
    database = {}

    with open('corp_data.csv', "r") as file:
        # len_of_file = len(file.readlines()) - 1
        # print(len_of_file)
        file.readline().split(';')
        for i in range(201):
            database[i] = file.readline().split(';')

    while True:
        print("Меню:")
        print("1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него")
        print('2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – '
                                                                                        '"макс", среднюю зарплату')
        print("3. Сохранить сводный отчёт")
        print("0. Выход")

        try:
            choice = int(input('Введите пункт:'))
        except ValueError:
            print('Вы ввели неверный пункт меню. Для выхода введите 0')


        match choice:
            case 0:
                print('Выход \n')
                break
            case 1:
                print('Иерархия команд \n')
                print_departmnet_structure(database)
            case 2:
                print('Сводный отчёт по департаментам \n')
                dep_review(database, 1)
            case 3:
                file = 'res_data.csv'
                save_review_to_csv(database, file_name=file)
                print(f'файл сохранен в {file} в директории проекта \n')
            case _:
                print("Неправильный ввод. Введите еще раз \n")