from enum import Enum
from Builder_pattern.CreamyBaconBuilder import CreamyBaconBuilder
from Builder_pattern.MargaritaBuilder import MargaritaBuilder
from Builder_pattern.Waiter import Waiter
from Factory_pattern.CoffeeMachine import CoffeeMachine
from Factory_pattern.Espresso import Espresso
from Factory_pattern.Latte import Latte

def validate_style1(builders1):
    try:
        pizza_style = input(
            'What pizza would you like, [m]argarita or [c]reamy bacon? ')
        builder1 = builders1[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder1)

def validate_style2(builders2):
    try:
        coffee_style = input(
            'What coffee would you like, [l]atte or [e]spresso? ')
        builder2 = builders2[coffee_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only latte (key l) and espresso (key e) are available')
        return (False, None)
    return (True, builder2)


def main():
    builders1 = dict(m = MargaritaBuilder, c = CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style1(builders1)
    print()

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza)) 
    print()
    print("------------------------------------------")
    
    builders2 = dict(l = Latte, e = Espresso)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style2(builders2)
    waiter.construct_coffee(builder)
    coffee = waiter.coffee

    print()
    print('Done with the {} coffee'.format(coffee))

if __name__ == '__main__':
    main()
    # coffeeMachine = CoffeeMachine()
    # coffee1 = coffeeMachine.make('Espresso')
    # print()
    # coffee2 = coffeeMachine.make('Latte')
