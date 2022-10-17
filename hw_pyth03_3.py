'''
Суть: принимаем список из float чисел. 
Ищем разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

ls = [1.1, 1.2, 3.1, 5, 10.01]  # float
def lsAftPoint (arr):
    aftPoint = []
    for i in range (len(arr)):
        aftPoint.append (int((arr[i]-(arr[i]//1))*100))    # *1000 !!!
    return aftPoint
print(lsAftPoint(ls))

def maxiMin (arr):
    minimal = min(arr)
    maximal = max(arr)
    differ = maximal-minimal
    return differ/100                                      # /1000
print (maxiMin(lsAftPoint(ls)))