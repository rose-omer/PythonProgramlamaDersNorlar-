import pandas as pd

print(pd.__version__)

seri = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(seri)
print(seri[["e"]])
print(seri[["a", "b", "c"]])
print(seri[2:4])
seri["d"] = 45
print(seri)

# Seri indeksleme ve dilimleme
seri = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(seri['c']) # 'c' indeksine karşılık gelen değeri getirir
print(seri[['a', 'b', 'e']]) # 'a', 'b' ve 'e' indekslerine karşılık gelen değerleri getirir


data = {"ögr": ["ahmet", "mehmet", "melike"],
        "sınıf": [10, 11, 12],
        "not": [23, 34, 54]}
dataframe = pd.DataFrame(data)
print(dataframe)

df = pd.DataFrame(data)
print(df.loc[2])

print(df[df["not"] > 30])

print(df[df["not"] >30]["ögr"])
df["Yas"] =[15,50,60]
print(df)
df.drop("Yas", axis=1, inplace=True)
print(df)
df.rename(columns={"not": "notlarrr"} , inplace=True)
print(df)


data = {'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru', 'Can', 'Deniz', 'Gizem',
                    'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül', 'Kadir', 'İrem', 'Ozan'],
        'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik'],
        'Not': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83, 94,81,84,90]}



df = pd.DataFrame(data)
print(df.head(5))

print(df.info)
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)

df =pd.read_csv('ornek.csv')
print(df)

import pip

pip.main(["install", "openpyxl"])
df =pd.read_excel("veri.xlsx", sheet_name="Sheet1")
print(df)
##data.to_csv("veri.csv", index=False)

'''
df =pd.DataFrame({"A": [1 ,2 ,None ,4 ,5 ],
                  "B":[None , 6 ,7 ,None ,9]})

df=df.dropna(implace =True)
print(df)'''
nerdy_one_df = pd.DataFrame({"A": [1,2, None, 4, 5],
                             "B": [None, 6, 7, None, 9]})

nerdy_one_df.dropna(inplace=True)
nerdy_one_df.fillna(nerdy_one_df["A"].mean(), inplace=True)
print(nerdy_one_df)
df = pd.DataFrame({'Tarih': ['2021-01-01', '2022-02-02', '2023-03-03'],
                   'Saat': ['12:00:00', '13:30:00', '15:45:00']})

# Tarih ve saat sütunlarını uygun veri türlerine dönüştürme
df['Tarih'] = pd.to_datetime(df['Tarih'])
df['Saat'] = pd.to_datetime(df['Saat'], format='%H:%M:%S').dt.time

# Veri çerçevesini görüntüleme
print(df)



# Veri çerçevesini oluşturma
df = pd.DataFrame({'Kategori': ['A', 'B', 'C'],
                   'Değer': [10, 20, 30]})

# Sütunları dönüştürme
df['Yeni_Kategori'] = df['Kategori'].apply(lambda x: x.lower())  # Kategori sütununu küçük harfe dönüştürme

# Veri çerçevesini görüntüleme
print(df)




# Veri çerçevesini oluşturma
df = pd.DataFrame({'Öğrenci': ['Ali', 'Ayşe', 'Mehmet'],
                   'Ders': ['Matematik', 'Fizik', 'Kimya'],
                   'Not': [90, 85, 95]})
df_pivot = df.pivot(index='Öğrenci', columns='Ders', values='Not')
# Dersleri sütunlara, öğrencileri satırlara dönüştürme
print(df_pivot)