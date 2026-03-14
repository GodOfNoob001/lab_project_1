import datetime

begin_t = datetime.datetime.now()
print("Программа работает")

end_t = datetime.datetime.now()
print(f'Код выполнился за {end_t - begin_t} сек.')