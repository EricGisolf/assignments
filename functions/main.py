# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'


# Add your code after this line
def greet(name):
    greetings = 'Hello, ' + name + '!'
    return greetings


print(greet('Eric'))


def add(a, b, c):
    numbers_list = [a, b, c]
    sum_of_numbers = sum(numbers_list)
    return sum_of_numbers


print(add(5, 3, 2))


def positive(x):
    var = x > 0
    return var


print(positive(0))


def negative(x):
    var = x < 0
    return var


print(negative(-3))
