'''
Суть: найти произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

ls = [2, 3, 4, 5, 6, 3, 5, 2, 0, 5]
resLs = []
def doubleExp (arr):
    global resLs
    while (len(arr) > 1):
        resLs.append (arr[0]*arr[-1])
        arr.pop(0)
        arr.pop(-1)
    if (len(arr) == 1):
        resLs.append (arr[0]**2)

def init():
    doubleExp(ls)
    print (resLs)

init()