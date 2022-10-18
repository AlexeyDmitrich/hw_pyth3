def switch ():

    print("\n ==================== МЕНЮ ===================")
    print(" |                                           |\n \
|  1. Сумма нечетных элементов списка       |\n \
|  2. Произведение пар чисел списка         | \n \
|  3. Поиск разницы между макс и мин        | \n \
|      значением дробной части элементов    |\n \
|  4. Перевод десятичного числа в двоичное  |\n \
|  5. [в стадии разработки]                 |\n \
|  0. Выход                                 |\n \
=============================================")

#    print("*** Нет адекватной реакции на повторный вызов ***")
    try:
        choise = int(input("Выберите пункт меню.\n"))
    except:
        print("Нет, вводить нужно целое число.\n")
        switch()
    match (choise):
        case 1:
            import hw_pyth03_1
            hw_pyth03_1.init()
            switch()
            return
        case 2:
            import hw_pyth03_2
            hw_pyth03_2.init()
            switch()
            return
        case 3:
            import hw_pyth03_3
            hw_pyth03_3  #.init()
            switch()
            return
        case 4:
            import hw_pyth03_4
            hw_pyth03_4  #.init()
            switch()
            return
        case 0:
            print("Завершение работы программы")
            return
        case _:
            print("Такого пункта меню пока нет(")
            switch()
            return

try:
    switch()
except:
    print("Соррян, произошла непредвиденная ситуация.")