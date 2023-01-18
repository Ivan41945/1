n=int(input('vvesti k-vo biletov '))
summa=0
for i in range(n):
    vzrst=int(input(f"vvesti vozrast {i+1} polzovatelya bileta "))
    if 18<=vzrst<25:
        summa+=990
    elif 25<=vzrst:
        summa+=1390
if n>3:
    summa*=0.9
input(summa)

