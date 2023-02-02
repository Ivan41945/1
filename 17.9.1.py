chisla = input("Ввести числа через пробел ")
spisok = [int(a) for a in chisla.split()]

num = int(input("Ввести число "))
if num % 1 == 0:
    spisok.append(num)
    print("Исходные данные ", spisok)

def my_sort(spisok):
    for i in range(len(spisok)):
        idx_min = i
        for j in range(i, len(spisok)):
            if spisok[j] < spisok[idx_min]:
                idx_min = j
        if i != idx_min:
            spisok[i], spisok[idx_min] = spisok[idx_min], spisok[i]
    return spisok

print("Ответ:", my_sort(spisok))