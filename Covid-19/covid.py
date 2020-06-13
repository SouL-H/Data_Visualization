import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Mevcut data
data=pd.read_csv("data.csv").iloc[:,8:]

pozitif = data[data['Label']== 'Positive']

           
gruplama =pozitif.groupby('Symptom').size()


goruntule =sns.countplot(x='Symptom', data=pozitif)
goruntule.set(xlabel='Semptomlar', ylabel='Hastalık Sayıusı',title="Covid-19 Semptom Grafiği")
plt.show()


