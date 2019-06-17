import pymysql
import matplotlib.pyplot as plt
import numpy as np
countries=[]
pop=[]
pop_percent=[]
total = 0
cnxn = pymysql.connect("localhost","root","","world")
cursor = cnxn.cursor()
cursor.execute("SELECT a.name as negara_ASEAN, a.population as populasi_negara, a.GNP, b.Name as Ibukota, b.Population from country a, city b WHERE a.Capital=b.ID HAVING negara_ASEAN = 'Brunei' OR negara_ASEAN = 'Cambodia' OR negara_ASEAN = 'East Timor' OR negara_ASEAN = 'Indonesia' OR negara_ASEAN = 'Laos' OR negara_ASEAN = 'Malaysia' OR negara_ASEAN = 'Myanmar' OR negara_ASEAN = 'Phillipines' OR negara_ASEAN = 'Singapore' OR negara_ASEAN = 'Thailand' OR negara_ASEAN = 'Vietnam'")
for row in cursor.fetchall():
    countries.append(row[0])
    pop.append(row[1])
    total+=row[1]
    print(row)
for elem in pop:
    pop_percent.append((elem/total)*100)
cnxn.commit()
cursor.close()
del cursor
cnxn.close()

plt.pie(pop_percent, labels=countries, startangle=90, autopct='%.1f%%')
plt.show()
