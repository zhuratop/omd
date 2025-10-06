# может убрать глобальную переменную
database = {}

with open('corp_data.csv', "r") as file:
    # len_of_file = len(file.readlines()) - 1
    # print(len_of_file)
    file.readline().split(';')
    for i in range(201):
        database[i] = file.readline().split(';')
# print(database)


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


# print_departmnet_structure(database)


def dep_review(db):
    dep_rev_db = {}
    cnt = 0
    for i in range(len(db) - 1):
        if db[i][1] not in dep_rev_db:
            dep_rev_db[cnt] = db[i][1]
        cnt += 1
    print(dep_rev_db)


dep_review(database)

