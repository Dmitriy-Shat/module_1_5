#immutable_var =('Привет:', True, 123)
#print(immutable_var)
#immutable_var[1] = False
#print(immutable_var) # Кортеж хранит ссылку на список, а не сам список, а по индексу
                     # мы пытаемся изменить само значение. а не ссылку на него

mutable_list = [1,2,3, 'String', True, 'a', 'b']
print(mutable_list)
mutable_list[-1] = 'e'
print(mutable_list)
