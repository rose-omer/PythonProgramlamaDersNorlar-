import pandas as pd
data = {'Öğrenci': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
        'Sınıf': [10, 11, 10, 12],
        'Not': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.loc[0]) # İlk satıra erişim
print(df.loc[1:2]) # 1. ve 2. satırlara erişim
print(df['Öğrenci']) # 'Öğrenci' sütununu seçme
print(df[df['Not'] > 85]) # Notu 85'ten büyük olan öğrencileri seçme
print()

df['Yaş'] = [15, 16, 15, 17]# 'Yaş' adında bir sütun eklenmesi
print(df)

df.drop('Not', axis=1, inplace=True)# Sütun silinmesi işlemi
print(df)

# Sütunu yeniden adlandırma
df.rename(columns={'Sınıf': 'Sınıf Seviyesi'}, inplace=True)
print(df)



newdata = {'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru', 'Can', 'Deniz', 'Gizem',
                    'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül', 'Kadir', 'İrem', 'Ozan'],
        'Ders': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
                 'Matematik', 'Fizik'],
        'Not': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83, 94, 81, 84, 90]}

df = pd.DataFrame(newdata)
# Veri setinin ilk 5 satırını görüntüleme
print(df.head())
# Veri setinin genel bilgilerini ve sütun veri tiplerini görüntüleme
print(df.info())
# Veri setinin sayısal sütunları için istatistiksel özet bilgileri görüntüleme
print(df.describe())
# Veri setinin satır ve sütun sayısını görüntüleme
print(df.shape)
#Sütunların adlarını gösterir.

print(df.columns)
# Sütunların veri tiplerini gösterir.
print(df.dtypes)


df = pd.DataFrame({'A': [1, 2, None, 4, 5],
                   'B': [None, 6, 7, None, 9]})
# Eksik verileri silme
df.dropna(inplace=True)
print(df)

df = pd.DataFrame({'A': [1, 2, None, 4, 5],
                   'B': [None, 6, 7, None, 9]})

# Eksik verileri belirli bir değerle doldurma
df.fillna(0, inplace=True)
print(df)