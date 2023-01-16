per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=float(input())

per_cent['ТКБ']=round(5.6 * money)
per_cent['СКБ']=round(5.9 * money)
per_cent['ВТБ']=round(4.28 * money)
per_cent['СБЕР']=round(4.0 * money)

print('список deposit значений',per_cent['ТКБ'],per_cent['СКБ'],per_cent['ВТБ'],per_cent['СБЕР'])
print('Максимальная сумма, которую вы можете заработать — ',max(per_cent.values()))
