import pandas as pd


typing_weakness = pd.read_csv(r"D:\Programming  and Coding\Pokemon Project\Pokemon Type Chart.csv")      #.T causign issues below
typing_weakness = typing_weakness.set_index("Type")

pokemon_data = pd.read_csv(r"D:\Programming  and Coding\Pokemon Project\pokemon_data.csv")

"""
ask for pokemon -- go by name (can do pokedex# if remove megas)
take that pokemon's typing and cross-refernce with weakness chart
if one typing, straightforward
2-typing, have to multiply 2 values
output damage multipliers    i.e.  Pokemon weaknesses are: xxxxx

"""


#merge = pd.merge(pokemon_data, typing_weakness, on= 'Type')
#merge = pd.merge(pokemon_data, typing_weakness, left_on="Other Type", right_on="Type")
#print(merge)


pokemon_name = input('\nWhat Pokemon would you like to know the weakness for? ')

#make sure first letter is capitalized each part of name  catch statement!?!?


pokemon_stats = pokemon_data[(pokemon_data.Name == pokemon_name)] ##.Name pulls the row
print(pokemon_stats)
print("\n")
#print('Weaknesses for ', pokemon_name, ' are:')


pokemon_type1 = pokemon_stats.at[pokemon_stats.index[0],"Type"]

pokemon_type2 = pokemon_stats.at[pokemon_stats.index[0],"Other Type"]


#print(typing_weakness[pokemon_type1])  #..._type1] ['Dark'] to give just a specific value
#print(typing_weakness[pokemon_type2])

print(pokemon_name + "\'s weakness chart:\n") 

if pd.isna(pokemon_type2):
    pokemon_weakness = typing_weakness[pokemon_type1]
    print(pokemon_weakness)
else:
    #multiply array.at(pokemontype1) by array.at(pokemontype2)
    array1 = typing_weakness[pokemon_type1]
    array2 = typing_weakness[pokemon_type2]
    pokemon_weakness = array1 * array2
    print(pokemon_weakness)


