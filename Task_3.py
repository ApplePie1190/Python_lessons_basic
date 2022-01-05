tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Андрей', 'Анна']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

school_students = ((tutors[i], klasses[i] if i < len(klasses) else None) for i in range(len(tutors)))

print(next(school_students))
print(next(school_students))
print(next(school_students))
print(next(school_students))
print(next(school_students))
print(next(school_students))
print(next(school_students))
print(next(school_students))
