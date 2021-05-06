# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name,greeting_template='Hello, <name>!'):

    greetings = greeting_template.replace('<name>',name)

    return greetings


def force(mass,body='earth'):

    surface_gravity = {
    'sun': 274,
    'jupiter': round(24.92, 1),
    'neptune': round(11.15, 1),
    'saturn': round(10.44, 1),
    'earth': round(9.798, 1),
    'uranus': round(8.87, 1),
    'venus': round(8.87, 1),
    'mars': round(3.71, 1),
    'mercury': 3.7,
    'moon': round(1.62, 1),
    'pluto': round(0.58, 1),
    }

    F = round(mass * surface_gravity[body], 1)

    return F


def pull(m1,m2,d):
    """
    Calculates the gravitational force between two bodies
    :param m1: mass of body 1 in kg
    :param m2: mass of body 2 in kg
    :param d: distance between the bodies in meters
    :return: force in Newton
    """

    G = 6.67e-11 # gravitational constant

    gravity = round(G * (m1 * m2) * d**-2, 2)

    return gravity



if __name__ == '__main__':
    greet('Eric')
    force(0.1, 'mercury')
    pull(0.1,5.972e24,6.371e6)