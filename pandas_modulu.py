import pandas as pd

# Veri setini okumak için
df = pd.read_csv("train.csv")

#  Sütunlardaki eksik değer sayısını göstermek için
print(" Her Sütundaki Eksik Değer Sayısı ")
print(df.isnull().sum())



#  Veri setinin ilk 5 satırı
print("\nVeri Setinin İlk 5 Satırı ")
print(df.head())

#  Veri seti hakkında bilgi 
print("\n Veri Seti Bilgisi ")
print(df.info())

#  sütunların istatistiksel özetii
print("\n İstatistiksel Özet ")
print(df.describe())