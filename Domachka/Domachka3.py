# Домашнее задание №3

qty = int(input("Укажите кол-во символов: "))
vid = input("Укажите тип символов: ")
orient = int(input("Укажите ориентацию линии 0 или 1: "))
while qty:
    if orient == 0:
        print(vid, end=" ")
        qty -= 1
    elif orient == 1:
        print(vid)
        qty -= 1