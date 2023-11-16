from datetime import date


filename = "text.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]
length = len(lines)
count=0
for i in lines:
    count+=len(i)
sr_symbols=int(count/length)


def decorator(func):
    def wrapper():
        style = input("Введите стиль: \n 1. С названием компании\n 2. С указанием даты и города в конце\n 3. С указанием названия\n 4. С указанием автора\n 5. Пункты 2-5\n")
        if str(style) == "1":
            name=input("Введите название компании\n")
            print(name.center(100,'*'),"\n\n")
            func()
        if str(style)=="2":
            city = input("Введите название города\n")
            func()
            print('\n',city.center(100),'\n',str(date.today()).center(100),"\n")
        if str(style)=="3":
            text_name=input("Введите Ф.И.О автора\n")
            print(text_name.center(100),"\n")
            func()
        if str(style) == "4":
            author=input("Введите имя автора\n")
            print(author.rjust(100),"\n")
            func()
        if str(style)=="5":
            city = input("Введите название города\n")
            text_name = input("Введите название текста\n")
            author = input("Введите имя автора\n")
            print(text_name.center(100), "\n")
            print(author.rjust(100), "\n\n")
            func()
            print('\n',city.center(100),'\n',str(date.today()).center(100),"\n")
    return wrapper


@decorator
def print_file():
    for l in lines:
        print(l)


print_file()
