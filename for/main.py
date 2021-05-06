from helpers import get_countries
import string


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Your code here. """

def shortest_names(list_of_country_names):

    minimum_name_length = len(min(list_of_country_names, key=len))

    short_list = []
    for name in list_of_country_names:
        if len(name) == minimum_name_length:
            short_list.append(name)

    return short_list

def most_vowels(list_of_country_names):
    list_of_country_names = [x.lower() for x in list_of_country_names]

    vowels = ['a','i','o','u','e']
    nr_vowels = []
    for name in list_of_country_names:
        counter = 0
        for letter in name:
            if letter in vowels:
                counter += 1
        nr_vowels.append(counter)

    top_three = []
    for i in range(3):

        max_vowels = max(nr_vowels)
        max_vowels_index = nr_vowels.index(max_vowels)
        top_three.append(list_of_country_names[max_vowels_index])

        nr_vowels[max_vowels_index] = 0

    return top_three


def alphabet_set(list_of_country_names):
    list_of_country_names = [x.lower() for x in list_of_country_names]

    alphabet = list(string.ascii_lowercase)

    countries_to_form_alphabet = []

    while alphabet != []:

        unique_letters_per_country = []

        for name in list_of_country_names:
            counter = 0
            for letter in alphabet:
                if letter in name:
                    counter += 1
            unique_letters_per_country.append(counter)

        max_letters = max(unique_letters_per_country)
        max_letters_index = unique_letters_per_country.index(max_letters)

        #print(max_letters, max_letters_index)
        #print(list_of_country_names[max_letters_index])

        for letter in list_of_country_names[max_letters_index]:
            if letter in alphabet:
                #print(letter)
                alphabet.remove(letter)

        countries_to_form_alphabet.append(list_of_country_names[max_letters_index])
        list_of_country_names.remove(list_of_country_names[max_letters_index])

    return countries_to_form_alphabet

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)

