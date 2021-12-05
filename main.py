# Código do dev aqui

from os import name


def sum_numbers(*numbers):
    return sum(numbers)

def get_multiplied_amount(mult, *numbers):
    result = 0
    for number in numbers:
        result += mult * number
    return result


def word_concatenator(*args):
    final_str = ''
    for word in args:
        final_str += word + ' '
    return final_str


def inverted_word_factory(*args):
    final_str = ''
    for word in args:
        final_str += word + ' '
    return final_str[::-1]


def dictionary_separator(**kwargs):
    keys_list = []
    values_list = []
    for key, value in kwargs.items():
        keys_list.append(key)
        values_list.append(value)
    result = (keys_list, values_list)
    return result

def dictionary_creator(*args, **kwargs):
    result = ''
    get_keys = []
    get_values = []
    dicttionary = {}
    if len(args) < len(kwargs):
        result = None
    else:
        get_keys = [key for key in args]
        get_values = [value for key, value in kwargs.items()]
        dictionary = dict(zip(get_keys, get_values))
        return dictionary



def purchase_logger(**kwargs):
    name = kwargs['name']
    price = kwargs['price']
    amount = kwargs['quantity']
    return f'Product {name} costs {price} and was bought {amount}'


def world_cup_logger(country, *args):
    return f'{country} - {sorted(args)}'
