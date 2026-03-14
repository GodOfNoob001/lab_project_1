import datetime

def input_array_once():
    numbers = []
    print("Введите число:")
    for i in range(10):
        num = int(input(f"Число под номером {i + 1}:"))
        numbers.append(num)
    return numbers

def input_array_another_path():
    data = input("Введите массив из 10 чисел через пробел: ").split()
    numbers = [int(x) for x in data[:10]]
    return numbers

def main():
    begin_t = datetime.datetime.now()
    print("Программа работает")
    choice = None
    while choice not in ('1', '2'):
        choice = input("Введите \'1\', если хотите ввести числа поочерёдно или \'2\', если хотите внести сразу весь массив: ").strip()
        if choice not in ('1', '2'):
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")

    numbers = []
    if choice == '1':
        numbers = input_array_once()
    else:
        numbers = input_array_another_path()

    numbers.sort()
    print("\nОтсортированные числа:")
    print(numbers)
    end_t = datetime.datetime.now()
    print(f'Код выполнился за {end_t - begin_t} сек.')

if __name__ == "__main__":
    main()