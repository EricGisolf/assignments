# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status):

    if location_of_the_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
        print('take cows to cowshed')

    elif location_of_the_cows == 'pasture' and cow_milking_status == True:
        print('take cows to cowshed')
        print('milk cows')
        print('take cows back to pasture')

    elif location_of_the_cows == 'cowshed' and cow_milking_status == True:
        print('milk cows')

    elif slurry_tank == True and location_of_the_cows == 'pasture' and weather != ('sunny' or 'windy'):
        print('take cows to cowshed')
        print('fertilize pasture')
        print('take cows back to pasture')

    elif slurry_tank == True and location_of_the_cows == 'cowshed' and weather != ('sunny' or 'windy'):
        print('fertilize pasture')

    elif grass_status == True and location_of_the_cows == 'pasture':
        print('take cows to cowshed')
        print('mow grass')
        print('take cows back to pasture')

    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'pasture':
        print('mow grass')

    else:
        print('wait')


