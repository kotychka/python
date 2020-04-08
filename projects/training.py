# Python 3
my_list = [1, 'two', 'a', 4, 'a']
# Попытка упорядочить/сравнить (< и >) несравнимые типы вызовет исключение, подробнее об этом
# в пункте «Сравнение последовательностей», статьи «Sequence (последовательность)»
# my_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

# Отсортируем «вручную», так чтобы 'а' были в конце.
my_list.sort(key=lambda val: val == 'a')  # None
print(my_list)