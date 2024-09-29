def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    for i in numbers:
        try:
            sum += i
        except TypeError as ex:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return sum,incorrect_data

def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
        num_count = len(numbers)-res[1]
        return res[0]/num_count
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать