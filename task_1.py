from math import sqrt

# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без
# использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное
# отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

vlue = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

average = sum(vlue) / len(vlue)
print(f'Среднее арифметическое: {average}')

std = sqrt(sum((x - sum(vlue) / len(vlue)) ** 2 for x in vlue) / (len(vlue)))
print(f'Среднее квадратичное отклонение: {round(std,2)}')

displaced = sum((x - sum(vlue) / len(vlue)) ** 2 for x in vlue) / (len(vlue))
print(f'Смещенная оценка дисперсии: {round(displaced,2)}')

no_displaced = sum((x - sum(vlue) / len(vlue)) ** 2 for x in vlue) / (len(vlue) - 1)
print(f'Несмещенная оценка дисперсии: {round(no_displaced, 2)}')
