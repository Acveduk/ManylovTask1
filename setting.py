def color():
    print(f"Выберите цвет:\n"
          f"1.) Красный\n"
          f"2.) Желтый\n"
          f"3.) Синий\n"
          f"4.) Черный\n"
          f"5.) Белый\n\n"
          f"Введите значение: ")
    value = str(input())
    match value:
        case "1":
            return "red"
        case "2":
            return "yellow"
        case "3":
            return "blue"
        case "4":
            return "black"
        case "5":
            return "white"
        case _:
            return color()


def font():
    print(f"Выберите цвет:\n"
          f"1.) Arial\n"
          f"2.) Calibri\n"
          f"3.) Candara\n"
          f"4.) Georgia\n"
          f"5.) Times New Roman\n\n"
          f"Введите значение: ")
    value = str(input())

    match value:
        case "1":
            return "Arial"
        case "2":
            return "Calibri"
        case "3":
            return "Georgia"
        case "4":
            return "Georgia"
        case "5":
            return "Times-New-Roman"
        case _:
            return font()
