# ---------------------------iterators/generators---------------------------------

def print_list_items(fruits):
    result = "[ "
    for fruit in fruits:
        result+= f"{{{fruit}}}, "
    return result+" ]"

def make_fruit_plural(fruits):
    return [fruit+"'s" for fruit in fruits]

def convert_list_to_dic(fruits):
    return tuple(fruit for fruit in fruits)

print(make_fruit_plural(["apple","orange","banana","cherry"]))
# ---------------------------decorators-----------------------------------------

from functools import wraps
from time import sleep

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = return_val_from_undecorated_function.upper() + "!!!"

        return emphasized

    return wrapper

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Oh Sure, "{orig_val}" sounds like a "great" idea'

    return wrapper


def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "On this day I do say, " + orig_val

    return wrapper

def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


@procrastinate
@proclaim
def say(txt):
    return txt

@sarcastic_decorator
@emphasize
def restaurant_suggestion(cuisine):
    return cuisine
# ---------------------------dunder methods ---------------------------------
class Restaurant:
    def __init__(self,meals = []):
        self.meals = meals

    def __bool__(self,meal):
        if meal not in self.meals:
            return False
        else:
            return True
        



if __name__ == "__main__":
    print(say('spam goes best with eggs.'))
