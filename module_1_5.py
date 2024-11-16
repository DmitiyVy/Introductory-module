immutable_var = (1, 2, 3, "Дмитрий", True, [2, 1])
print(immutable_var)
# immutable_var[3] = "Иван" - Компилятор выдает ошибку TypeError: object does not support item assignment
# immutable_var[4] = False  - Потому что в отличии от списка, в кортеже объекты неизменяемы
# immutable_var[3][-1] = "Й"
immutable_var[5][0] = 1 # - Изменить элименты можно только внутри элемента типа list
print(immutable_var)
print(end='\n')

mutable_list = [4, 5, 6, "Иван", False, [4,3]]
print(mutable_list)
mutable_list[ : ] = [1, 2, 3, "Дмитрий", True, [2,1]]
print(mutable_list)
