
def taskOne(string):

    print(string[2])        # Вывод третьего символа

    print(string[-2])       # Вывод предпоследнего символа

    print(string[:5])       # Вывод первых пяти символов

    print(string[:-2])      # Вывод всей строки, кроме последних двух символов

    print(string[::2])      # Вывод всех символов с четными индексами

    print(string[1::2])     # Вывод всех символов с нечетными индексами

    print(string[::-1])     # Вывод всех символов в обратном порядке

    print(string[-1::-2])   # Вывод всех символов через один в обратном порядке, начиная с последнего

    print(len(string))      # Вывод длины строки


def taskTwo(string):
    list = string.split()   #делаем из строки список 
    count = len(list)       # получаем длинну 
    print("Количество слов:", count)

def taskThree(string):
    str = string[len(string) // 2:] + string[:len(string) // 2]

    # более понятно

    # length = len(string) длинна строки
    # half = length // 2 половина строки

    # first_half = string[:half] первая часть
    # second_half = string[half:] вторая
    # str = second_half + first_half Конечная


    print(str)

def taskFour(string):

    list = string.split()
    first = string[0]
    list = list[1:]
    list.append(first)
    string = " ".join(list)
    
    print(string)

def taskFive(string):
    first = string.find('f')
    last = string.rfind('f')
    
    if string.find('f') == -1:
        print("Буква 'f' не найдена")
    elif string.find('f') == string.rfind('f'):
        print(string.find('f'))
    else:
        print(string.find('f'))
        print(string.rfind('f'))

def taskSix(string):
    first_f = string.find('f')                      # находим индекс первого вхождения буквы f
    if first_f == -1:                               # если буква f не встречается в строке
        print(-2)
    else:
        second_f = string.find('f', first_f + 1)    # ищем второе вхождение, начиная с позиции после первого вхождения
    if second_f == -1:                              # если буква f встречается только один раз
        print(-1)
    else:
        print(second_f) 


def taskSeven(string):
    first = string.find('h') # находим индекс первого вхождения буквы h
    last = string.rfind('h') # находим индекс последнего вхождения буквы h
    new_s = string[:first] + string[last+1:]

    print(new_s) 



def taskEight(string):

    #   СДЕЛАТЬ

    print(string) 



def taskNine(string):

    new_s = string.replace('1', 'one')
    print(new_s) 

def taskTen(string):
    new_s = string.replace('@', '')
    print(new_s)



def taskEleven(string):

    #   СДЕЛАТЬ

    print(string)    



def taskTwelve(string):
    new_s= ""
    for i in range(len(string)):
        if i % 3 != 0: 
            new_s += string[i]
    print(new_s)
my_string  = "Abrakadabra"

taskOne(my_string)

my_string_two = "In the hole in the ground there lived a hobbit"

taskTwo(my_string_two)

taskThree(my_string)

my_string_three ="Q WERRTYUIOP"

taskFour(my_string_three)

str5 = "comfort"

taskFive(str5)