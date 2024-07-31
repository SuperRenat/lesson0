my_list = ['apple', 'banana', 'coconut', 'peach', 'Ananas']
print(my_list)
# print(my_list[0], my_list[4]) - можно вот так вывести на экран
print(my_list[0:5:4])
# print(my_list[2], my_list[3], my_list[4]) - и тут тоже можно вот так вывести на экран
print(my_list[2:])
my_list[2] = 'kiwi'
print(my_list)

my_dict = {'Apple': "Яблоко", 'Banana': "Банан", 'Coconut': "Кокос", 'Peach': "Персик", 'Ananas': "Ананас", }
print(my_dict)
print('Перевод: ', my_dict['Apple'])
print('Перевод: ', my_dict['Coconut'])
my_dict['Orange'] = "Апельсин"
# my_dict.update({'Orange': "Апельсин"}) - можно и вот так
print(my_dict)
