immutable_var = (['Привет','земляне'], 9, 8, True)
print(immutable_var)
print(type(immutable_var))
# immutable_var - это кортеж
# его нельзя изменить, если попытаться его изменить, то выдаст ошибку, напрмер:
# immutable_var[3] = 3
print('Кортеж (tuple_) неизменяемый')
mutable_list = ['Питонище', 4, 6, False]
print(mutable_list)
print(type(mutable_list))
mutable_list[0]='Питон'
mutable_list[1]='может'
mutable_list[2]='изменить'
mutable_list[3]='Список'
print(mutable_list)
