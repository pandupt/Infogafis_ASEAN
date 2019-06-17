import pymysql
import matplotlib.pyplot as plt
import numpy as np
countries=[]
area=[]
per_area=[]
total_area=0
cnxn = pymysql.connect("localhost","root","","world")
cursor = cnxn.cursor()
cursor.execute("SELECT a.name as negara_ASEAN, a.SurfaceArea, a.GNP, b.Name as Ibukota, b.Population from country a, city b WHERE a.Capital=b.ID HAVING negara_ASEAN = 'Brunei' OR negara_ASEAN = 'Cambodia' OR negara_ASEAN = 'East Timor' OR negara_ASEAN = 'Indonesia' OR negara_ASEAN = 'Laos' OR negara_ASEAN = 'Malaysia' OR negara_ASEAN = 'Myanmar' OR negara_ASEAN = 'Phillipines' OR negara_ASEAN = 'Singapore' OR negara_ASEAN = 'Thailand' OR negara_ASEAN = 'Vietnam'")
for row in cursor.fetchall():
    countries.append(row[0])
    area.append(row[2])
    total_area+=row[2]
    print(row)
for elem in area:
    per_area.append((elem/total_area)*100)
cnxn.commit()
cursor.close()
del cursor
cnxn.close()

plt.pie(per_area, labels=countries, startangle=200, autopct='%.1f%%')
plt.show()
