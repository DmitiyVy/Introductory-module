grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
print("Список студентов по алфавиту: ", students_list)

gpa = [sum(sublist)/len(sublist) for sublist in grades]
print("Список с средним баллом: ",gpa)

gpa_students = {students_list[i]: gpa[i] for i in range(len(students_list))}
print("Итоговый список: ", gpa_students)
