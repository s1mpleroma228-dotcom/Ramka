def ramka(ширина, висота):
    print("*" * ширина)
    for i in range(висота - 2):
        print("*" + " " * (ширина - 2) + "*")
    print("*" * ширина)

ramka(10, 5)