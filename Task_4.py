def thesaurus(*args):
    name_book = {name[0]: [] for name in sorted(args)}
    for name in sorted(args):
        if name.startswith(name[0]):
            name_book[name[0]].append(name)
    return name_book


def thesaurus_adv(*args):
    name_book = {
        surname[surname.find(' ') + 1]: {
            name[0]: [] for name in sorted(args) if name[name.find(' ') + 1] == surname[surname.find(' ') + 1]
        } for surname in sorted(args)
    }
    for name in sorted(args):
        if name.startswith(name[0]):
            name_book[name[name.find(' ') + 1]][name[0]].append(name)
    return name_book


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Андрей"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
