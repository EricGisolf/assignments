# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(list_of_filmnames):
    sorted_list = sorted(list_of_filmnames)
    return sorted_list


def won_golden_globe(film):
    gg_wins = ['Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']
    gg_wins = [x.lower() for x in gg_wins]
    we_have_a_winner = film.lower() in gg_wins
    return we_have_a_winner

def remove_toto_albums(list_of_albums):
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in between', '35th Anniversary – Live in Poland',
                   'Toto XIV', 'Old is New', '40 Tours Around the Sun - Live in Holland']

    #toto_albums = [x.lower() for x in toto_albums]
    #list_of_albums = [x.lower() for x in list_of_albums]

    for film in list_of_albums:
        if film in toto_albums:
            list_of_albums.remove(film)

    if list_of_albums == []:
        return print('empty list!')

    return print(list_of_albums)

