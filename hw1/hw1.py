list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list)

# crescator
list_cres = sorted(list)
print(list_cres)

# descrescator
list_des = sorted(list, reverse=True)
print(list_des)

# elemente pare
# list_par = list_cres[1::2]
# print(list_par)
print(sorted(list)[1::2])

# elemente impare
# list_impar = list_cres[::2]
# print(list_impar)
print(sorted(list)[::2])

# multiplii de 3
for i in range(len(list)):
    if (list[i] % 3 == 0):
        print(list[i], end=' ')

