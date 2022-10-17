'''
Суть: преобразовывать десятичное число в двоичное. 
'''

ten = int(input("Введите десятичное число"))
arr = []
def binArr (ten):
    global arr
    temp = ten
    # print(temp)
    # print(arr)
    if (ten == 0):
        arr.insert(0, 0)
        # print(temp)
        # print(arr)
        return
    elif (ten == 1):
        arr.insert(0, 1)
        # print(temp)
        # print(arr)

    else:
        if (ten % 2 == 0):
            arr.insert(0, 0)
            # print(temp)
            # print(arr)
            temp -= (ten // 2)
            # print(temp)
            # print(arr)
            return binArr (temp)
        else:
            arr.insert(0, 1)
            temp -= ((ten // 2)+1)
            # print(temp)
            # print(arr)
            return binArr (temp)
binArr(ten)
#print(arr) 

def arrToInt (arr):
#    print (arr)
    temp = 0
    for i in range(len(arr)):
        temp = (temp+arr[i])*10
    return int(temp/10)

binaryInt = arrToInt(arr)
print(binaryInt)