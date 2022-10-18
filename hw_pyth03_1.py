'''
Суть: принимаем список из нескольких чисел. 
Ищем сумму элементов списка, стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

ls = [2, 3, 5, 9, 3, 1, 2, 1, 3, 1, 2, 1]
try:
    def blackIndex (arr):
        counter = 0
        for i in range(len(arr)):
            if (i % 2 != 0):
                counter += arr[i]
        return counter
except:
    print("Произошла ошибка")
def init ():
    val = blackIndex(ls)
    print("установленный массив: ", ls)
    print ("сумма нечетных элементов: ", val)

init()
