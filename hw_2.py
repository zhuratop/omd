
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


def dep_review(db):
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
    for dep in dep_rev_db.keys():
        print(f'Департамент: {dep}\n численность: {dep_rev_db[dep]["amount"]} | '
              f'мин. зп: {dep_rev_db[dep]["min_sal"]} | '
              f'макс зп: {dep_rev_db[dep]["max_sal"]} | '
              f'средн. зп: {dep_rev_db[dep]["avg_sal"]}')
        dep_rev_db[dep]['avg_sal'] = int(dep_rev_db[dep]['sum_sal'] / dep_rev_db[dep]['amount'])

    # print(dep_rev_db)

if __name__ == '__main__':
    # dep_review(database)
    database = {}

    with open('corp_data.csv', "r") as file:
        # len_of_file = len(file.readlines()) - 1
        # print(len_of_file)
        file.readline().split(';')
        for i in range(201):
            database[i] = file.readline().split(';')
    dep_review(database)
    # for i in range(10):
    #     print(database[i])
    # print_departmnet_structure(database)
