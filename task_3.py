# На соревновании по биатлону один из трех спортсменов стреляет и попадает в
# мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8,
# для третьего — 0.6. Найти вероятность того, что выстрел произведен:
# a). первым спортсменом
# б). вторым спортсменом
# в). третьим спортсменом.

chance = 1 / 3
full = chance * 0.9 + chance * 0.8 + chance * 0.6

p1 = (chance * 0.9) / full
print(f'Вероятность того, что выстрел произведен первым спортсменом: {round(p1, 3)} или {round(p1, 3)*100}%')

p2 = (chance * 0.8) / full
print(f'Вероятность того, что выстрел произведен вторым спортсменом: {round(p2, 3)} или {round(p2, 3)*100}%')

p3 = (chance * 0.6) / full
print(f'Вероятность того, что выстрел произведен третьим спортсменом: {round(p3, 3)} или {round(p3, 3)*100}%')
