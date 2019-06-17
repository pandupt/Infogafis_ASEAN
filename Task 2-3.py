import pymysql
import matplotlib.pyplot as plt
import numpy as np
countries=[]
gnp=[]

cnxn = pymysql.connect("localhost","root","","world")
cursor = cnxn.cursor()
cursor.execute("SELECT a.name as negara_ASEAN, a.population as populasi_negara, a.GNP, b.Name as Ibukota, b.Population from country a, city b WHERE a.Capital=b.ID HAVING negara_ASEAN = 'Brunei' OR negara_ASEAN = 'Cambodia' OR negara_ASEAN = 'East Timor' OR negara_ASEAN = 'Indonesia' OR negara_ASEAN = 'Laos' OR negara_ASEAN = 'Malaysia' OR negara_ASEAN = 'Myanmar' OR negara_ASEAN = 'Phillipines' OR negara_ASEAN = 'Singapore' OR negara_ASEAN = 'Thailand' OR negara_ASEAN = 'Vietnam'")
for row in cursor.fetchall():
    countries.append(row[0])
    gnp.append(row[2])
    print(row)
cnxn.commit()
cursor.close()
del cursor
cnxn.close()

index = np.arange(len(countries))
plt.bar(countries, gnp)
plt.xlabel('Negara', fontsize=5)
plt.ylabel('Gross National Product (US$)', fontsize=5)
plt.xticks(index, countries, fontsize=5, rotation=30)
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.show()
