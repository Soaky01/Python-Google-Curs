list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list)

# crescator
list_ord = sorted(list)
print(list_ord)

# descrescator
list_des = sorted(list, reverse=True)
print(list_des)

# elemente pare
# list_par = list_ord[1::2]
# print(list_par)
print(sorted(list)[1::2])

# elemente impare
# list_impar = list_ord[::2]
# print(list_impar)
print(sorted(list)[::2])

# multiplii de 3
for i in range(len(list)):
    if (list[i] % 3 == 0):
        print(list[i])
