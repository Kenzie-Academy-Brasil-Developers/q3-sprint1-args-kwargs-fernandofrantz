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
    counter = 0
    for word in args:
        if counter < len(args) -1:
            final_str += word + ' '
        else:
            final_str += word
        counter += 1
    return final_str


def inverted_word_factory(*words):
    final_str = ''
    counter = 0
    for word in words:

        if counter <= len(words):
            final_str += word + ' '
        else:
            final_str += word
        counter += 1
    final_str = final_str[::-1]
    return final_str[1:]




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
    years = sorted(args)
    final_str = f'{country} - '
    counter = 0
    for year in years:
        if counter < len(args) -2:
            final_str += f'{year}, '
        elif counter < len(args) -1:
            final_str += f'{year} e '
        else:
            final_str += f'{year}'
        counter += 1
    return final_str
