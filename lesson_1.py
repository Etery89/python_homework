import os
import random

"""Вывести таблицу умножения в виде. 
1 x 1 = 1
1 x 2 = 2
..
1 x 10 = 10
— 
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N
Параметр N задается с клавиатуры 
(или в виде аргумента скрипта, по желанию). 
Между разделами вывести разделитель в виде 5 девисов 
"""


def print_myltiplication_table(number):
    if number > 10:
        raise ValueError("Таблица умножения оперирует с цифрами от 1-го до 10-ти.")
    for i in range(1, number + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {j * i}")
        print("-----")



"""Реализовать функцию print_directory_contents(path). 
Функция принимает имя директории и выводит ее содержимое, 
включая содержимое всех поддиректории (рекурсивно вызывая саму себя). 
Использовать os.walk нельзя, 
но можно использовать os.listdir и os.path.isfile"""


def print_directory_contents(path):
    list_dir_from_path = os.listdir(path)
    # print(list_dir_from_path)
    for name in list_dir_from_path:
        path_name = os.path.join(path, name)
        if name[0] == "." or name[0] == "_":
            continue
        if os.path.isfile(path_name):
            print(name)
        else:
            print("-----")
            print(f'directory {name}')
            print_directory_contents(path_name)


"""Разработать целочисленный генератор случайных чисел. 
В функцию передавать начальную и конечную границу диапазона генерации 
(выдавать значения из диапазона включая концы). Заполнить этими данными словарь. 
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, 
а значенbе сгенеренное случайное число. Вывести содержимое словаря. 
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random. 
"""


def get_dict_random_value(num_elements, left_lim, right_lim):
    gen = (random.randint(left_lim, right_lim + 1) for i in range(num_elements))
    result_dict = {}
    for _ in range(num_elements):
        result_dict[f"elem_{_}"] = next(gen)
    return result_dict


"""Написать программу «Банковский депозит». 
Клиент банка делает депозит на определенный срок. 

В зависимости от суммы и срока вклада определяется процентная ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых). 

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах), 
а на выходе возвращать сумму вклада на конец срока.

Усовершенствовать программу «Банковский депозит». 
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. 
Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. 
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""

SMALL_DEPOSIT = 10000
AVERAGE_DEPOSIT = 100000
LARGE_DEPOSIT = 1000000

rates = {
    SMALL_DEPOSIT: {6: 5, 12: 6, 24: 5},
    AVERAGE_DEPOSIT: {6: 6, 12: 7, 24: 6.5},
    LARGE_DEPOSIT: {6: 7, 12: 8, 24: 7.5}
}

def calc_deposit(size, rate, term, monthly_size):
    if not monthly_size:
        return size + (size * rate * term * 30 / 365) / 100
    else:
        result_profeet = 0
        for month in range(term):
            size += monthly_size
            result_profeet += (size * rate * (month * 30) / 365) / 100
            # print(result_profeet)
        # print(result_profeet)
        return size + result_profeet



def get_rate(deposit_rates, deposit_term):
    rate = 0
    terms = list(deposit_rates.keys())
    if deposit_term <= terms[0]:
        rate = deposit_rates[terms[0]]
    elif terms[1] <= deposit_term < terms[2]:
        rate = deposit_rates[terms[1]]
    else:
        rate = deposit_rates[terms[2]]
    return rate


def get_deposit(deposit_size, deposit_term, monthly_size=0):
    if isinstance(deposit_size, int) or isinstance(deposit_size, float):
        if deposit_size <= SMALL_DEPOSIT:
            rate = get_rate(rates[SMALL_DEPOSIT], deposit_term)
        elif SMALL_DEPOSIT < deposit_size <= AVERAGE_DEPOSIT:
            rate = get_rate(rates[AVERAGE_DEPOSIT], deposit_term)
        else:
            rate = get_rate(rates[LARGE_DEPOSIT], deposit_term)
        # print(rate)
        return int(calc_deposit(deposit_size, rate, deposit_term, monthly_size))
    else:
        raise ValueError("Величину депозита необходимо задавать числом.")


if __name__ == "__main__":
    print_myltiplication_table(6)
    # print_myltiplication_table(11)
    test_path = os.path.dirname(os.path.abspath(__file__))
    print_directory_contents(test_path)

    dict_values = get_dict_random_value(20, 10, 200)
    print(dict_values)

    print(get_deposit(100000, 6, monthly_size=500))
    print(get_deposit(100000, 6))
