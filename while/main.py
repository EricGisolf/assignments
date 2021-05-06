from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def unique_koala_facts(nr_of_koala_facts):

    unique_facts = []

    while len(unique_facts) < nr_of_koala_facts:

        x = random_koala_fact()

        if x not in unique_facts:
            unique_facts.append(x)

        if len(unique_facts) == 29:
            break

    return unique_facts


def num_joey_facts():

    max_nr = 10
    facts = []
    nr_joeys = 0
    nr_of_reps = 0

    while nr_of_reps < max_nr:
        x = random_koala_fact()
        if x in facts:
            nr_of_reps += 1
        facts.append(x)

    for fact in facts:
        if 'joey' in fact:
            nr_joeys += 1

    return nr_joeys


def koala_weight():

    bool = 0

    while bool == 0:

        fact = random_koala_fact()

        if 'weigh' and 'kg' in fact:
            weight = fact[fact.find('kg')-2:fact.find('kg')]

            bool = 1

    return weight


if __name__ == '__main__':
    unique_koala_facts(40)
    num_joey_facts()
    koala_weight()
    #print(random_koala_fact())
