import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pokemon_data = pd.read_csv(r"D:\Programming  and Coding\Pokemon Project\pokemon_data.csv")
pokemon_data = pokemon_data[pokemon_data["Name"].str.contains("Mega") == False]

generation_1 = pokemon_data[pokemon_data.Generation == 1]
generation_2 = pokemon_data[pokemon_data.Generation == 2]
generation_3 = pokemon_data[pokemon_data.Generation == 3]
generation_4 = pokemon_data[pokemon_data.Generation == 4]
generation_5 = pokemon_data[pokemon_data.Generation == 5]
generation_6 = pokemon_data[pokemon_data.Generation == 6]
generation_7 = pokemon_data[pokemon_data.Generation == 7]
generation_8 = pokemon_data[pokemon_data.Generation == 8]

avg_gen1_total = np.mean(generation_1.Total)
avg_gen2_total = np.mean(generation_2.Total)
avg_gen3_total = np.mean(generation_3.Total)
avg_gen4_total = np.mean(generation_4.Total)
avg_gen5_total = np.mean(generation_5.Total)
avg_gen6_total = np.mean(generation_6.Total)
avg_gen7_total = np.mean(generation_7.Total)
avg_gen8_total = np.mean(generation_8.Total)



#avg total stats by generation
x = [1,2,3,4,5,6,7,8]
height = [avg_gen1_total,avg_gen2_total,avg_gen3_total,avg_gen4_total,avg_gen5_total,avg_gen6_total,avg_gen7_total,avg_gen8_total,]
plt.bar(x, height, color = ['indigo', 'silver',])
plt.xlabel('Generation')
plt.ylabel('AVG Total Base Stats')
plt.title('Pokemon AVG Base Stats Per Generation (Omitting Mega\'s)')
for i in range(len(x)):
    plt.text(i+1,height[i], round(height[i]), ha ='center', va = 'bottom')

plt.ylim([0,500])

plt.show()












"""
pokemon_data = pd.read_csv(r"D:\Programming  and Coding\Pokemon Project\pokemon-data.csv")
pokemon_data = pokemon_data[pokemon_data["Name"].str.contains("Mega") == False]
#pokemon_dataframe = pd.DataFrame(pokemon_data)
print(pokemon_data)

pokemon_data['Generation'].value_counts().plot(kind='barh')
plt.show()
"""

"""
X = list(pokemon_dataframe.iloc[:,1])
Y = list(pokemon_dataframe.iloc[:,11])
plt.bar(X, Y)
plt.show()
"""