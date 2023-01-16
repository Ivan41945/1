per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=float(input())

per_cent['ТКБ']=round(0.056*money)
per_cent['СКБ']=round(0.059 * money)
per_cent['ВТБ']=round(0.0428 * money)
per_cent['СБЕР']=round(0.04 * money)

print('список deposit значений',per_cent['ТКБ'],per_cent['СКБ'],per_cent['ВТБ'],per_cent['СБЕР'])
print('Максимальная сумма, которую вы можете заработать — ',max(per_cent.values()))
