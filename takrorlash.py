# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# x, y, z = 1, 2, 3
# a = 5  
# b = 6 
# c = 7

# sonlar = [9, 8, 7, 6, 5, 4, 3, 2]

# #sonlar = list(range(1,11))
# for son in range(8):
#     print(f"{son} ning kvadrati {son**2} ga teng")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]
borlar = []  #ro'yxatdagi bor taomlar 
yuqlar = []  #menudagi yuq taomlar

for taom in buyurtmalar:
    if taom in menu:
        borlar.append(taom)
        # print(f"Menuda {taom} bor")
    else:
        yuqlar.append(taom)
        # print(f"Kechirasiz, menuda {taom} yo'q")
        
print(f"Menyuda { borlar } bor, {yuqlar} esa yuq")




print('TEKSHIR')