# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
Spain_most_spoken_language = 'Castilian Spanish'
Switzerland_most_spoken_language = 'German (or Swiss German)'
print(Spain_most_spoken_language == Switzerland_most_spoken_language)

Spain_most_prevalent_religion = 'Roman Catholic'
Switzerland_most_prevalent_religion = 'Roman Catholic'
print(Spain_most_prevalent_religion == Switzerland_most_prevalent_religion)

Spain_capital_name_length = len('Madrid')
Switzerland_capital_name_length = len('Bern')
print(Spain_capital_name_length != Switzerland_capital_name_length)

Spain_GDP = 1.778e12
Switzerland_GDP = 5.8e11
print(Switzerland_GDP > Spain_GDP)

Spain_population_growth_perc = 0.67
Switzerland_population_growth_perc = 0.66
print((Spain_population_growth_perc and Switzerland_population_growth_perc) <1)

Spain_population = 5.0e7
Switzerland_population = 8.4e6
print((Spain_population or Switzerland_population) >1e7)

print((Spain_population or Switzerland_population) >1e7 and not (Spain_population and Switzerland_population) >1e7)