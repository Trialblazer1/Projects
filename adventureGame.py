import time
import random

hand = []
villain = ['zombie', 'cyclops', 'dragon', 'pirate', 'troll']
selection = random.choice(villain)


def stop():
    time.sleep(1)


def print_pause(message, sec = 1):
    print(message)
    time.sleep(sec)


def intro():
    print_pause('You find yourself in a dark dungeon.')
    print_pause('In front of you are two passageways.')
    print_pause('In your hand you hold your trusty'
                '(but not very effective) dagger')


def print_1():
    print('You are about to knock when the door opens '
          'and out steps a', selection)
    stop()
    print('Eep! this is a', selection, "'s house")
    stop()
    print('and the', selection, 'attacks you!')
    stop()


def print_2():
    print('As the', selection, 'moves to attack you, '
          'you unsheath your new sword!')
    stop()
    print('The', selection, 'runs away, and you have '
          'rid the town of', selection, '.')
    stop()
    print('You are Victorious!')
    stop()


def decision():
    dec = input("would you like to play again (y/n)?").lower()
    if dec == 'y':
        print_pause('Excellent Re-starting the game...')
        field()
    elif dec == 'n':
        print_pause('Thank you!')
    else:
        print_pause('please enter y to play again (or) n to exit the game')
        decision()


def field():
    choice = input('Enter 1 to knock on the door of the house.\n'
                   'Enter 2 to peer into the cave.\n'
                   'What would you like to do?\n'
                   'Please enter 1 or 2.\n')
    if choice == '1':
        house()
    elif choice == '2':
        cave()
    else:
        field()


def house():
    print_1()
    if 'sword' not in hand:
        print_pause('You feel a bit under-prepared '
                    'with only having a tiny dagger')
    win_lose()


def cave():
    print_pause('You peer cautiously into the cave')
    if 'sword' in hand:
        print_pause("You have been here before and gotten "
                    "all the good stuff! It's just an empty cave now.")
    else:
        print_pause('It turns out to be a very small cave')
        print_pause('Your eye catches the glint of a metal behind the rock.')
        print_pause('You have found the magical Sword, Hurray!')
        print_pause('You discard your old dagger and'
                    'take the new Sword with you.')
        hand.append('sword')
    print_pause("You walk back to the field")
    field()


def win_lose():
    opt = input('would you like to (1) fight? or (2) run away?\n')
    if opt == '1':
        if 'sword' in hand:
            print_2()
        else:
            print('Your teeny-tiny dagger is no '
                  'match to the', selection, 'power!')
            stop
            print_pause('You are defeated!')
        decision()
    elif opt == '2':
        print_pause("You run back into the field. "
                    "Luckily you don't seem to have been followed")
        field()
    else:
        win_lose()


intro()
field()
