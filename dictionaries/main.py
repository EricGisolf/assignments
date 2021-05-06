from helpers import get_countries

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'

def create_passport(name,date_of_birth,place_of_birth,height,nationality):

    passport = {}
    passport['name'] = name
    passport['date_of_birth'] = date_of_birth
    passport['place_of_birth'] = place_of_birth
    passport['height'] = height
    passport['nationality'] = nationality

    return passport


def add_stamp(passport,country):

    countries = []
    countries.append(country)

    if 'stamps' in passport and country != passport['nationality'] and country not in passport['stamps']:
        passport['stamps'].append(country)

    if 'stamps' not in passport and country != passport['nationality']:
        passport['stamps'] = countries

    return passport


#def check_passport(passport,country,allow,not_allow):






if __name__ == '__main__':
    create_passport('Eric','1981-08-07','Leidschendam','1.83','Netherlands')
    add_stamp(create_passport('Eric','1981-08-07','Leidschendam','1.83','Netherlands'),'Belgium')
    #check_passport()